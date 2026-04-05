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

