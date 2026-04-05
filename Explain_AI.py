import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt

# 1. Load the "Brain" and the Data
with open('oncology_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load a few rows of data to explain
import duckdb
con = duckdb.connect('oncology_registry.db')
X = con.execute("SELECT mean_radius, mean_texture, mean_perimeter FROM cancer_registry LIMIT 100").df()

# 2. THE SHAP "INTERROGATOR"
# SHAP explains how the model thinks
explainer = shap.LinearExplainer(model, X)
shap_values = explainer.shap_values(X)

# 3. VISUALIZE THE "WHY"
# This chart shows which feature pushes the diagnosis toward 'Malignant'
shap.summary_plot(shap_values, X, plot_type="bar")
plt.savefig('ai_explanation_impact.png') # Save the proof for GitHub
plt.show()

print("✅ SUCCESS: AI 'Thought Process' mapped and saved as 'ai_explanation_impact.png'.")
