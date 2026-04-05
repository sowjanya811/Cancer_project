import pandas as pd
import duckdb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle # To save the "Brain" for our Dashboard later

# 1. Connect to your GitHub-verified Registry
con = duckdb.connect('oncology_registry.db')
df = con.execute("SELECT * FROM cancer_registry").df()

# 2. FEATURE SELECTION (Using the "Gears" we found in EDA)
# We pick the high-signal features: perimeter, texture, and radius
X = df[['mean_radius', 'mean_texture', 'mean_perimeter']]
y = df['diagnosis'].map({'Malignant': 1, 'Benign': 0}) # 1 = Risk, 0 = Safe

# 3. THE SPLIT (80% Study, 20% Exam)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TRAINING THE BRAIN (Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. THE EXAM (Testing on patients the AI has NEVER seen)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"🎯 AI BRAIN ACCURACY: {accuracy * 100:.2f}%")
print("\n📋 CLINICAL PERFORMANCE REPORT:")
print(classification_report(y_test, predictions))

# 6. SAVE THE BRAIN (So our Dashboard can use it tomorrow)
with open('oncology_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ SUCCESS: AI Brain trained and saved as 'oncology_model.pkl'.")
con.close()
