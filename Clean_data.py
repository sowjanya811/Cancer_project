import pandas as pd

def standardize():
    # 1. Load the raw data (usually headerless)
    df = pd.read_csv('raw_oncology_data.csv', header=None)

    # 2. Define the Medical Schema
    medical_headers = [
        'patient_id', 'raw_diagnosis_code', 
        'mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area'
    ]
    # Apply headers to the columns we have
    df.columns = medical_headers + [f'extra_{i}' for i in range(len(df.columns) - len(medical_headers))]

    # 3. THE STANDARDIZATION STEP (The "Translator")
    # We keep 'raw_diagnosis_code' (M/B) and create 'diagnosis' (Malignant/Benign)
    df['diagnosis'] = df['raw_diagnosis_code'].map({
        'M': 'Malignant', 
        'B': 'Benign',
        0: 'Malignant',
        1: 'Benign'
    })

    # 4. Save for the Registry
    df.to_csv('standardized_oncology_data.csv', index=False)
    print("✅ SUCCESS: Data standardized. 'M/B' converted to 'Malignant/Benign'.")

if __name__ == "__main__":
    standardize()
