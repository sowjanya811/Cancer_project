# 🎗️ Breast Cancer Classification & Explainability Pipeline

**A full end-to-end machine learning project to classify breast tumors as malignant or benign — with an interactive dashboard and AI explainability built in.**

---

## 📌 Project Summary

This project builds a clinical decision-support pipeline for early breast cancer detection using the **Wisconsin Diagnostic Breast Cancer (WDBC)** dataset. It covers everything from raw data ingestion to a trained, explainable model and a live interactive dashboard — structured as a real-world data science workflow.

The pipeline is written entirely in Python and is organized into modular scripts, each handling one stage of the process. The trained model is saved as a reusable `.pkl` file, enabling deployment in downstream applications.

---

## 🔍 The Problem This Project Solves

Breast cancer is the most commonly diagnosed cancer among women globally. Early and accurate diagnosis — distinguishing a **malignant** tumor from a **benign** one — is critical. Delayed or incorrect diagnosis leads to:

- Unnecessary biopsies and surgical procedures (false positives)
- Missed treatment windows for aggressive tumors (false negatives)
- Significant financial and emotional cost to patients and healthcare systems

Clinicians currently rely on manual review of cell measurements from fine needle aspirate (FNA) biopsies. This process is time-consuming, subject to human variability, and difficult to scale.

This project provides a **data-driven, explainable classification model** that can assist oncologists and diagnostic labs in making faster, more consistent decisions — with full transparency into *why* the model made a given prediction.

---

## 👥 Who Benefits

| Stakeholder | How They Benefit |
|---|---|
| **Oncologists & Radiologists** | A second-opinion tool that flags high-risk cases for priority review |
| **Diagnostic Laboratories** | Faster triage of biopsy samples, reduced manual review load |
| **Hospital Administrators** | Reduced cost from unnecessary procedures driven by false positives |
| **Patients** | Earlier detection, faster treatment initiation, better outcomes |
| **Healthcare Data Science Teams** | A reusable, modular pipeline they can adapt for other cancer types |

---

## 💰 Business Impact & ROI

Unnecessary cancer-related procedures — unnecessary biopsies, extended diagnostic workups — cost the U.S. healthcare system an estimated **$4–8 billion annually**. A model with high specificity directly reduces this waste.

| Business Metric | Impact |
|---|---|
| **Reduced false positive rate** | Fewer unnecessary biopsies → lower procedural cost per patient |
| **Earlier malignant detection** | Earlier-stage treatment is significantly less expensive than late-stage intervention |
| **Clinician time savings** | Automated first-pass screening reduces manual review time per case |
| **Scalability** | Pipeline can process thousands of records with no incremental cost |

Even a **5–10% reduction in false positive biopsies** across a mid-sized hospital system translates to hundreds of thousands of dollars in avoided procedural costs annually, plus measurable improvement in patient quality of care.

---

## 📊 Key Performance Indicators (KPIs)

The model is evaluated against the following clinical and technical KPIs:

| KPI | Description | Target |
|---|---|---|
| **Model Accuracy** | % of correct classifications (malignant / benign) | ≥ 90% |
| **Sensitivity (Recall)** | % of actual malignant cases correctly identified | ≥ 92% — minimizes missed cancers |
| **Specificity** | % of actual benign cases correctly identified | ≥ 88% — minimizes unnecessary procedures |
| **Precision** | Of predicted malignant cases, how many are truly malignant | ≥ 90% |
| **F1 Score** | Harmonic mean of precision and recall | ≥ 0.90 |
| **SHAP Feature Impact** | Which cell features most strongly drive malignant predictions | Visualized per prediction |

> **Note:** In clinical contexts, **sensitivity is prioritized over accuracy** — a missed malignant diagnosis is far more costly than an unnecessary follow-up.

---

## 🛠️ Pipeline Architecture

The project is organized into 7 modular Python scripts, each representing one stage of the data science pipeline:

```
Cancer_project/
│
├── ingest_data.py          # Stage 1: Load raw WDBC data, store in DuckDB registry
├── Clean_data.py           # Stage 2: Handle missing values, standardize features
├── Predective_EDA.py       # Stage 3: Exploratory analysis — distributions, correlations, class balance
├── Building_pipeline.py    # Stage 4: Feature engineering and preprocessing pipeline
├── Training_model.py       # Stage 5: Train logistic regression model, evaluate, save model
├── Explain_AI.py           # Stage 6: SHAP explainability — visualize feature impact
└── APP_dashboard.py        # Stage 7: Interactive dashboard for real-time prediction
│
├── oncology_registry.db        # DuckDB database storing cleaned registry data
├── oncology_model.pkl          # Saved trained model (reusable for dashboard / API)
├── raw_oncology_data.csv       # Raw input data
├── standardized_oncology_data.csv  # Cleaned, standardized data
└── wdbc.names                  # Dataset feature definitions
```

---

## ⚙️ Algorithms & Technologies Used

### Machine Learning
- **Logistic Regression** (Scikit-learn) — Binary classification: Malignant (1) vs. Benign (0)
- **Train/Test Split** — 80/20 split with `random_state=42` for reproducibility
- **Feature Selection** — High-signal features identified via EDA: `mean_radius`, `mean_texture`, `mean_perimeter`

### Explainability
- **SHAP (SHapley Additive exPlanations)** — `LinearExplainer` to quantify each feature's contribution to individual predictions
- SHAP summary bar plots saved as `ai_explanation_impact.png`

### Data & Storage
- **DuckDB** — Lightweight analytical database for storing and querying the oncology registry
- **Pandas / NumPy** — Data manipulation and feature engineering
- **Pickle** — Model serialization for dashboard reuse

### Evaluation Metrics
- `accuracy_score`, `classification_report` (precision, recall, F1) from Scikit-learn

### Dashboard
- **APP_dashboard.py** — Interactive interface for real-time predictions using the saved model

### Dataset
- **Wisconsin Diagnostic Breast Cancer (WDBC)** — UCI Machine Learning Repository
- 569 patient records, 30 numeric features derived from FNA biopsy cell measurements
- Binary target: **Malignant** / **Benign**

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/sowjanya811/Cancer_project.git
cd Cancer_project

# 2. Install dependencies
pip install pandas numpy scikit-learn duckdb shap matplotlib

# 3. Run the pipeline in order
python ingest_data.py
python Clean_data.py
python Predective_EDA.py
python Building_pipeline.py
python Training_model.py
python Explain_AI.py
python APP_dashboard.py
```

---

## 👩‍💻 Author

**Sowjanya K** — Healthcare Data Professional | Aspiring Data Scientist
- GitHub: [github.com/sowjanya811](https://github.com/sowjanya811)
- LinkedIn: [linkedin.com/in/sowjanya-k-157a5212a](https://linkedin.com/in/sowjanya-k-157a5212a)

---

## 📁 Related Projects

- [EpicCare Analytics](https://github.com/sowjanya811/EpicCare-Analytics) — Predictive analytics workflows for clinical healthcare data

---

*This project is part of an independent data science portfolio focused on applying machine learning to real-world healthcare problems.*
