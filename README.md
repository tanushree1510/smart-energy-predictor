# 🏡 Energy Consumption Predictor

This is a machine learning-powered web application that predicts household energy consumption based on indoor and outdoor environmental parameters using an XGBoost regression model.

---

## 📌 Project Overview

- **Objective**: Predict energy consumption (`Appliances`) using input environmental variables.
- **Model Used**: XGBoost Regressor
- **Frontend**: Streamlit
- **Language**: Python
- **Deployment**: Local (can be extended to cloud platforms like Streamlit Cloud, Heroku, or AWS)

---

## ⚙️ Features

- Interactive user input interface
- Real-time prediction display
- Easy-to-use sliders for input values
- Trained on real environmental data

---

## 🧠 Machine Learning Pipeline

1. **Data Cleaning & Preprocessing**
   - Handled missing/null values
   - Normalized feature scales
2. **Feature Engineering**
   - Selected relevant features: 
     `['T1', 'RH_1', 'T2', 'RH_2', 'T_out', 'RH_out', 'Visibility', 'Windspeed', 'Tdewpoint', 'Press_mm_hg']`
3. **Model Training**
   - Model: `XGBoostRegressor`
   - Target: `Appliances` (energy usage)
4. **Evaluation**
   - RMSE, R², MAE used for performance checks

---

## 🚀 Running the App Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/energy-consumption-predictor.git
cd energy-consumption-predictor
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📊 Example Inputs

| Feature      | Value  |
|--------------|--------|
| T1           | 20.0   |
| RH_1         | 19.8   |
| T2           | 20.3   |
| RH_2         | 20.0   |
| T_out        | 17.5   |
| RH_out       | 40.1   |
| Visibility   | 60.0   |
| Windspeed    | 5.0    |
| Press_mm_hg  | 1015   |
| Tdewpoint    | 8.5    |

---

## 📁 File Structure

```
energy-consumption-predictor/
│
├── app.py                    # Streamlit frontend
├── xgboost_energy_model.pkl  # Trained model
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview
```

---

## 👤 Author

- **Tanushree Indresh**
- AI & Data Science Engineer | 5th Semester  
- Email: tanushreebi15@gmail.com  
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 📌 To Do / Future Enhancements

- [ ] Add weather API for real-time feature input
- [ ] Deploy on Streamlit Cloud / Heroku
- [ ] Add multiple model comparison (Linear, RF, XGBoost)
- [ ] Visualize predictions over time

---

## 💡 Acknowledgements

- UCI Energy Efficiency Dataset
- Scikit-Learn, XGBoost, Streamlit Libraries

## 🌐 Live Demo

👉 [Try the Smart Energy Predictor Web App](https://smart-energy-predictor-6pjsgmzqp5ibmwplbs7bbz.streamlit.app/)

---

## 🏃‍♀️ How to Run Locally

Make sure you have Python 3.9+ installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tanushree1510/smart-energy-predictor.git
   cd smart-energy-predictor


Built using Streamlit • Predicts future energy consumption with ML models like XGBoost, Random Forest, and Linear Regression.


