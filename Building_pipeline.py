import pandas as pd
import duckdb

df = pd.read_csv('standardized_oncology_data.csv')
con = duckdb.connect('oncology_registry.db')

# Logic: If a tumor is Malignant AND larger than average (15mm), it's 'CRITICAL'
con.execute("""
    CREATE OR REPLACE TABLE cancer_registry AS 
    SELECT *,
    CASE 
        WHEN diagnosis = 'Malignant' AND mean_radius > 15 THEN 'CRITICAL'
        WHEN diagnosis = 'Malignant' THEN 'URGENT'
        ELSE 'MONITOR'
    END AS clinical_priority
    FROM df
""")

print("✅ Database Enhanced: 'Clinical Priority' logic added.")
con.close()
