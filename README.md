# 🏡 FUNDUS

<p align="center">

### AI-Powered Real Estate Intelligence Platform

Predict property prices, analyze market trends, and discover similar properties using Machine Learning.

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

</p>

---

## 📖 Overview

FUNDUS is an end-to-end Machine Learning application built for real estate price prediction and property analytics.

The application predicts property prices in **Gurugram** using machine learning while providing rich visual analytics, interactive dashboards, investment insights, and an intelligent property recommendation system.

Designed as a portfolio-quality project, FUNDUS combines data science, machine learning, visualization, and web development into a single application.

---

# ✨ Features

### 💰 Property Price Prediction

Predict property prices using an optimized **ExtraTrees Regressor** pipeline.

- Price estimation
- Log-transformed predictions
- Realistic valuation

---

### 📊 Interactive Analytics Dashboard

Explore the real estate market through interactive visualizations.

- Price Distribution
- Sector-wise Price Analysis
- Feature Correlation Heatmap
- BHK Distribution
- Price vs Area Analysis
- Interactive Charts

---

### 🏘️ Smart Property Recommendation

Find similar properties using a hybrid similarity engine.

The recommendation system combines multiple similarity matrices including:

- Location Similarity
- Feature Similarity
- Price Similarity

to recommend the most relevant properties.

---

### 📍 Nearby Property Search

Search properties within a custom radius from any selected location.

Features include

- Radius Search
- Distance Calculation
- Nearby Properties
- Interactive Selection

---

### 📈 Investment Insights

Provides useful information for buyers and investors including

- Market Trends
- Expensive Sectors
- Feature Importance
- Property Comparison

---

# 🧠 Machine Learning Pipeline

```
Raw Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Column Transformer
      │
      ├── Standard Scaler
      ├── Ordinal Encoder
      ├── One Hot Encoder
      └── Target Encoder
      │
      ▼
ExtraTrees Regressor
      │
      ▼
Price Prediction
```

---

# 📂 Project Structure

```
FUNDUS
│
├── app.py
├── Pages/
│   ├── home.py
│   ├── page2.py
│   ├── page3.py
│   └── page4.py
│
├── component/
│
├── Models/
│
├── notebooks/
│
├── Data/
│
├── assets/
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Web Framework | Streamlit |
| Machine Learning | Scikit-Learn |
| Model | ExtraTrees Regressor |
| Feature Engineering | ColumnTransformer |
| Encoding | TargetEncoder, OneHotEncoder, OrdinalEncoder |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Deployment | Render |

---

# 📊 Dataset

The model is trained on residential property data from **Gurugram**.

Features include

- Property Type
- Sector
- Bedrooms
- Bathrooms
- Balcony
- Furnishing Status
- Age of Property
- Built-up Area
- Servant Room
- Store Room
- Luxury Category
- Floor Category

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/khushraj17/FUNDUS-app.git
```

Move into the project

```bash
cd FUNDUS-app
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---
<!-- 
# 📷 Screenshots

### 🏠 Home

_Add Screenshot_

---

### 💰 Price Prediction

_Add Screenshot_

---

### 📊 Analytics

_Add Screenshot_

---

### 🏘️ Recommendation System

_Add Screenshot_

--- -->

# 🎯 Future Improvements

- AI Chat Assistant
- Property Comparison
- Mortgage Calculator
- Rental Yield Prediction
- Interactive Map Search
- Personalized Investment Recommendations
- Explainable AI Predictions

---

# 👨‍💻 Developer

**Khushraj Rane**

B.Tech Artificial Intelligence & Machine Learning

GitHub:
https://github.com/khushraj17

LinkedIn:
https://www.linkedin.com/in/khushraj-rane-772abb30b/

---

# ⭐ Support

If you found this project useful,

⭐ Star the repository

🍴 Fork it

🐞 Report issues

💡 Suggest new features

---

<p align="center">

Made with ❤️ using Python, Streamlit and Machine Learning

</p>