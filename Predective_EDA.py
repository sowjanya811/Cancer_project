import pandas as pd
import duckdb
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to your new GitHub-verified registry
con = duckdb.connect('oncology_registry.db')
df = con.execute("SELECT * FROM cancer_registry").df()

# Convert diagnosis back to numbers for math (M=1, B=0)
df['target'] = df['diagnosis'].map({'Malignant': 1, 'Benign': 0})

# Create a Correlation Map to find "Predictor Features"
plt.figure(figsize=(10, 8))
# We only look at the main medical features we standardized
features = ['target', 'mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area']
correlation_matrix = df[features].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Oncology Feature Correlation: Finding Predictors")
plt.show()

print("✅ EDA Complete: We have identified the strongest features for our Risk Model.")
con.close()
