# Titanic Survival Prediction 🚢

## Overview
This project predicts passenger survival on the Titanic using machine learning.  
The dataset was taken from the **Kaggle Titanic competition**.

## Dataset
- Source: [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)  
- Files used: `train.csv`, `test.csv`, `gender_submission.csv`

## Approach
- Dropped irrelevant columns (`PassengerId`, `Name`, `Ticket`, `Cabin`)  
- Encoded categorical features (`Sex`, `Embarked`) and scaled numeric ones  
- Trained a `RandomForestClassifier` inside a pipeline for consistent preprocessing  

## Evaluation
- Accuracy is printed by comparing predictions on `test.csv` with labels from `gender_submission.csv`.

## ⚙️ How to Run
1. Clone the repository and open the notebook (`.ipynb`) in Jupyter Notebook or JupyterLab.  
2. Install dependencies from `requirements.txt`:  
   ```bash
   pip install -r requirements.txt