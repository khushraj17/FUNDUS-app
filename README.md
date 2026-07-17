# 🏡 FUNDUS – AI-Powered Real Estate Analytics & Recommendation System

FUNDUS is an intelligent real estate platform that combines **Machine Learning**, **Data Analytics**, and **Interactive Visualization** to help users analyze the Gurgaon real estate market, predict property prices, and discover similar properties using an AI-powered recommendation engine.

Built using **Python**, **Streamlit**, **Scikit-learn**, and **Plotly**, FUNDUS provides an intuitive interface for buyers, investors, and real estate enthusiasts to explore properties more effectively.

---

## 🚀 Features

### 🏠 Property Price Prediction
- Predict property prices using a trained Machine Learning model.
- User-friendly prediction interface.
- Supports multiple property features.

### 🤖 Property Recommendation System
- Hybrid recommendation engine.
- Location-aware property recommendations.
- Explore similar properties with one click.
- Uses weighted cosine similarity.

### 📍 Location-Based Search
- Search nearby properties within a custom radius.
- Distance-based filtering.
- Interactive property exploration.

### 📊 Real Estate Analytics
- Interactive charts and graphs.
- Price distribution analysis.
- Sector-wise insights.
- Feature correlation analysis.
- Market trend visualization.

### 🎨 Modern Streamlit UI
- Multi-page application.
- Responsive design.
- Interactive property cards.
- Easy navigation.

---

# 🧠 Recommendation Engine

The recommendation engine combines three similarity matrices into a hybrid similarity score.

```
<!-- 
Final Score

= (0.5 × Cosine Similarity Matrix 1)
+ (0.8 × Cosine Similarity Matrix 2)
+ (1.0 × Cosine Similarity Matrix 3)
```

This approach improves recommendation quality by considering multiple property characteristics.

---

<!-- # 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Model Storage | Pickle |
| Development | Jupyter Notebook |

---

# 📂 Project Structure

```
FUNDUS-app/
│
├── app.py
├── page1.py
├── page2.py
├── page3.py
├── page4.py
│
├── location_df.pkl
├── cosine_sim1.pkl
├── cosine_sim2.pkl
├── cosine_sim3.pkl
├── ETRmodel.pkl
│
├── requirements.txt
├── README.md
└── assets/
```

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/khushraj17/FUNDUS-app.git
```

Move into the project directory

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

# 💻 Modules

- 🏠 Home
- 📊 Analytics Dashboard
- 💰 Price Prediction
- 📍 Location Search
- 🤖 Property Recommendation

---

# 📸 Screenshots

Add screenshots here.

Example:

```
assets/home.png

assets/analytics.png

assets/prediction.png

assets/recommendation.png
```

---

# 📈 Future Improvements

- Property Images
- Google Maps Integration
- User Authentication
- Wishlist
- Advanced Filters
- Personalized User Profiles
- Deep Learning Recommendation System
- Real-time Property Listings
- API Integration

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning
- Recommendation Systems
- Feature Engineering
- Content-Based Filtering
- Regression Models
- Data Visualization
- Streamlit Development
- Interactive Dashboard Design
- Model Deployment

---

# 📦 Requirements

```
streamlit
pandas
numpy
plotly
scikit-learn
```

---

# 👨‍💻 Author

**Khushraj Rane**

B.Tech Artificial Intelligence & Machine Learning

GitHub: https://github.com/khushraj17

---

## ⭐ If you like this project

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. 

It helps support the project and motivates future improvements. -->