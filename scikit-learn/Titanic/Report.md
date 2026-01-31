# Titanic Survival Prediction Report 🚢

## Dataset Choice
I selected the **Titanic dataset** from the Kaggle competition *“Titanic: Machine Learning from Disaster.”*  
This dataset is widely used for beginner machine learning projects because it combines numeric and categorical features, includes missing values, and has a clear binary target (`Survived`). It provides a good balance of complexity and accessibility.

---

## Findings
- Dropped irrelevant columns (`PassengerId`, `Name`, `Ticket`, `Cabin`).  
- Encoded categorical features (`Sex`, `Embarked`) and scaled numeric ones using a `ColumnTransformer`.  
- Evaluated models using accuracy, precision, recall, F1‑score, ROC‑AUC, and confusion matrix.  
- Best accuracy achieved: **~0.90**.

---

## Model Comparison
- **RandomForestClassifier**  
  - Accuracy: ~0.90  
  - Strong baseline, robust performance.  
  - Scaling not required but included for consistency.  

- **HistGradientBoostingClassifier**  
  - Accuracy: slightly lower but competitive.  
  - Handles missing values natively, reducing preprocessing complexity.  
  - Good ROC‑AUC performance.
 
---

## Conclusion
This project demonstrates a complete ML workflow: preprocessing, training, evaluation, and comparison.  
The **RandomForestClassifier** provided the best accuracy (~83%), while **HistGradientBoostingClassifier** offered robustness to missing values. Both are suitable starting points for Kaggle submissions, with room for improvement through feature engineering and advanced boosting methods.