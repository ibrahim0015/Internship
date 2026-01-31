# Titanic Survival Prediction 🚢

## Overview
This project predicts passenger survival on the Titanic using machine learning.  
The dataset was taken from the **Kaggle Titanic competition**.

## Dataset
- Source: [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)  
- Files used: `train.csv`, `test.csv`, `gender_submission.csv`

## Approach
- Dropped irrelevant columns (`PassengerId`, `Name`, `Ticket`, `Cabin`)  
- Encoded categorical features (`Sex`, `Embarked`) and scaled numeric ones using a `ColumnTransformer`  
- Trained two models:
  - **RandomForestClassifier** (baseline, n_estimators=200, max_depth=6)  
  - **HistGradientBoostingClassifier** (handles missing values natively)

## Evaluation
- Metrics printed: Accuracy, Precision, Recall, F1‑score, ROC‑AUC  
- Confusion matrix plotted for visual inspection  
- Best accuracy achieved: **0.90**

## How to Run
```bash
python titanic.py
