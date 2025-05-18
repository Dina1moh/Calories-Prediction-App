# 🔥 Calories Burn Prediction

This project predicts the number of calories burned during exercise based on biometric and activity data using machine learning regression models. The dataset contains user information like age, gender, height, weight, and workout-related data such as duration, heart rate, and body temperature.

---

## 📂 Dataset

- **Source:** [Kaggle - Calories Burned Dataset](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos)
- **Files:**
  - `exercise.csv` - Features dataset
  - `calories.csv` - Target dataset (calories burned)

---

## 🧪 Models Used

Several regression models were trained and evaluated:

- **SGDRegressor**
- **Lasso Regression**
- **Ridge Regression**
- **Elastic Net**
- **K-Nearest Neighbors**
- **Support Vector Regressors (Linear, Polynomial, RBF)**
- **Random Forest Regressor** (with RandomizedSearchCV)
- **XGBoost Regressor** (with GridSearchCV)

---

## 🧠 Best Model

The best performance was achieved using **XGBoost Regressor**, tuned with GridSearchCV.  
✅ **R² Score**: 0.9993  
✅ **RMSE**: 1.6868

---

## 📊 EDA Highlights

- **Gender Distribution**
- **Calories Distribution**
- **Age Distribution**
- **Duration vs Calories Scatter Plot**
- **Calories vs Gender Boxplot**
- **Feature Correlation Heatmap**

---

## ⚙️ Data Preprocessing

- **Numerical Columns:** Imputed using median and scaled with StandardScaler.
- **Categorical Columns:** Imputed with most frequent value and one-hot encoded.
- **Target (Calories):** Scaled with StandardScaler.

Preprocessors and model are saved using `joblib`.

---

---

## 🚀 Inference API (Flask)

### 🔹 Endpoint: `/predict`
- **Method:** POST
- **Request Body (JSON):**
```json
{
  "Gender": "Male",
  "Age": 25,
  "Height": 175,
  "Weight": 70,
  "Duration": 30,
  "Heart_Rate": 120,
  "Body_Temp": 37.0
}


{
  "predicted_calories": 245.89
}


