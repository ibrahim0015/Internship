# Machine Learning Models on Classic Datasets

## What I Built
This project explores machine learning workflows using scikit-learn on well-known datasets (Iris, Wine, and Breast Cancer).  
I practiced data preprocessing, visualization, model training, evaluation, and hyperparameter tuning with GridSearchCV.  
The goal was to understand how different models behave and how techniques like scaling and pipelines improve performance.

---

## Models Tried
1. **K-Nearest Neighbors (KNN)**  
   - Applied on the Iris dataset.  
   - Hyperparameter tuning with GridSearchCV (tested different values of `n_neighbors`).  

2. **Logistic Regression**  
   - Applied on the Wine dataset (with and without scaling).  
   - Also applied on the Breast Cancer dataset using a Pipeline with `StandardScaler`.  

---

## Final Test Accuracies
- **KNN (Iris dataset)**: ~1.0 (100% accuracy on test set after tuning).  
- **Logistic Regression (Wine dataset)**:  
  - Without scaling: ~0.72  
  - With scaling: ~0.97  
- **Logistic Regression (Breast Cancer dataset, with pipeline)**: ~0.96  

---

## Model Choice
I would choose **Logistic Regression with scaling** as the preferred model.  
It consistently achieved high accuracy across different datasets, and scaling ensured fair contribution of all features.  
Compared to KNN, Logistic Regression is more interpretable and scales better to larger datasets, making it a stronger choice for real-world applications.