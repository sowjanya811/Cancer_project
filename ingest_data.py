import pandas as pd
from sklearn.datasets import load_breast_cancer

def ingest():
    # Load the official curated medical dataset
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    # Save raw version for your records
    df.to_csv('raw_oncology_data.csv', index=False)
    print("✅ Step 1: Raw data ingested and saved as 'raw_oncology_data.csv'.")
    return df

if __name__ == "__main__":
    ingest()