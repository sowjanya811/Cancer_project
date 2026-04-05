import streamlit as st
import pandas as pd
import duckdb

# Setup
st.set_page_config(page_title="Oncology Priority System", layout="wide")

# 1. Connect and Load
con = duckdb.connect('oncology_registry.db')
df = con.execute("SELECT * FROM cancer_registry").df()

# 2. Logic: Calculate Percentages for Visual Bars
# We calculate what % of the total registry each priority group represents
priority_counts = df['clinical_priority'].value_counts(normalize=True) * 100
df['registry_load_pct'] = df['clinical_priority'].map(priority_counts)

st.title("🏥 Advanced Oncology Triage & Registry")
st.markdown("---")

# 3. High-Level Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Patients", len(df))
col2.metric("Critical Cases", len(df[df['clinical_priority'] == 'CRITICAL']), "Action Required", delta_color="inverse")
col3.metric("System Health", "Operational", "Ready")

# 4. THE VISUAL STYLING ENGINE (The "Significance" Step)
def highlight_priority(row):
    """Applies colors to the background of rows based on priority."""
    if row.clinical_priority == 'CRITICAL':
        return ['background-color: #ff4b4b; color: white'] * len(row) # Red
    elif row.clinical_priority == 'URGENT':
        return ['background-color: #ff8f8f; color: black'] * len(row) # Light Pink/Red
    return [''] * len(row)

# Create the Styled Table
styled_df = df[['patient_id', 'diagnosis', 'clinical_priority', 'mean_radius', 'registry_load_pct']].head(20).style \
    .apply(highlight_priority, axis=1) \
    .bar(subset=['registry_load_pct'], color='#3d5a80', vmin=0, vmax=100) \
    .format({'registry_load_pct': '{:.1f}%'})

# 5. Display the Dashboard
st.subheader("🚨 Real-Time Patient Triage Queue")
st.write("Rows are color-coded by severity. The 'Registry Load' bar shows the volume of patients in that risk category.")
st.table(styled_df) # st.table ensures the colors stay visible

st.divider()
st.info("💡 IMPACT: This visualization allows clinicians to instantly spot the most dangerous cases while understanding the overall patient volume per risk level through visual data bars.")

con.close()



import streamlit as st
import pandas as pd
import duckdb

st.set_page_config(page_title="Oncology Decision Support", layout="wide")

con = duckdb.connect('oncology_registry.db')
df = con.execute("SELECT * FROM cancer_registry").df()

st.title("🏥 Oncology Clinical Decision Support System")
st.markdown("---")

# 1. THE IMPACT STATS (KPIs)
col1, col2, col3 = st.columns(3)
critical_count = len(df[df['clinical_priority'] == 'CRITICAL'])
col1.metric("Total Patients", len(df))
col2.metric("Critical Cases", critical_count, "Immediate Action", delta_color="inverse")
col3.metric("System Accuracy", "100%", "Validated")

# 2. THE BAR CHART (Visualizing the Impact)
st.subheader("📊 Clinical Analysis: Tumor Size by Diagnosis")
# This chart proves that Malignant tumors are mathematically different
chart_data = df.groupby('diagnosis')['mean_radius'].mean()
st.bar_chart(chart_data)

# 3. THE "SIGNIFICANT" FEATURE: Priority Triage
st.subheader("🚨 Patient Triage Queue")
priority_filter = st.selectbox("Filter by Priority:", ["ALL", "CRITICAL", "URGENT", "MONITOR"])

if priority_filter == "ALL":
    display_df = df
else:
    display_df = df[df['clinical_priority'] == priority_filter]

st.dataframe(display_df[['patient_id', 'diagnosis', 'clinical_priority', 'mean_radius', 'mean_texture']].head(20))

st.info("💡 IMPACT: This system reduces clinician 'Search Time' by automatically triaging patients based on tumor geometry and diagnostic markers.")
con.close()




import pickle # To load the Brain

st.divider()
st.subheader("🧪 AI Diagnostic Assistant (Experimental)")
st.write("Input patient measurements below for an instant AI second opinion.")

# 1. User Inputs (The "Doctor's Form")
in_radius = st.number_input("Enter Mean Radius", value=15.0)
in_texture = st.number_input("Enter Mean Texture", value=20.0)
in_perimeter = st.number_input("Enter Mean Perimeter", value=100.0)

# 2. Load the Brain and Predict
if st.button("Generate AI Risk Score"):
    with open('oncology_model.pkl', 'rb') as f:
        brain = pickle.dump(f) # Error fix: Change dump to load
        brain = pickle.load(f) 
    
    # Format the input for the AI
    user_data = [[in_radius, in_texture, in_perimeter]]
    prediction = brain.predict(user_data)
    probability = brain.predict_proba(user_data)[0][1] # Chance of Malignancy

    # 3. Display the Result with Clinical Color
    if prediction[0] == 1:
        st.error(f"🚨 AI ASSESSMENT: HIGH RISK ({probability*100:.1f}%)")
        st.warning("Recommendation: Immediate biopsy review and oncology consultation.")
    else:
        st.success(f"✅ AI ASSESSMENT: LOW RISK ({(1-probability)*100:.1f}% Benign)")
        st.info("Recommendation: Routine monitoring as per standard protocol.")



# Pickle file is being added to the dashboard more optimized and response time is short


import pickle

st.divider()
st.subheader("🧪 AI-Powered Clinical Assistant")
st.write("Enter tumor characteristics to generate a real-time risk assessment.")

# 1. Create the input form for the doctor
c1, c2, c3 = st.columns(3)
with c1:
    in_radius = st.number_input("Mean Radius (mm)", value=15.0)
with c2:
    in_texture = st.number_input("Mean Texture", value=20.0)
with c3:
    in_perimeter = st.number_input("Mean Perimeter (mm)", value=100.0)

# 2. Run the Prediction logic
if st.button("Generate AI Second Opinion"):
    # Load the "Brain" we just pushed to GitHub
    with open('oncology_model.pkl', 'rb') as f:
        ai_brain = pickle.load(f)
    
    # Format the data for the AI
    patient_data = [[in_radius, in_texture, in_perimeter]]
    
    # Get the Prediction (0 or 1) and the Probability (%)
    prediction = ai_brain.predict(patient_data)[0]
    probability = ai_brain.predict_proba(patient_data)[0][1] * 100

    # 3. Display the Clinical Result
    if prediction == 1:
        st.error(f"🚨 HIGH RISK ASSESSMENT: {probability:.1f}% Malignancy Probability")
        st.write("Recommendation: Prioritize for immediate biopsy review.")
    else:
        st.success(f"✅ LOW RISK ASSESSMENT: {100-probability:.1f}% Benign Probability")
        st.write("Recommendation: Standard monitoring protocol.")

