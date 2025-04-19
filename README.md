# 🫀 Heart Disease Prediction Web App

This is a **Heart Disease Prediction** web application built using **Flask**, **Scikit-learn**, and a **Machine Learning model** trained on healthcare data. Users can enter medical parameters, and the model predicts whether they are at risk of heart disease.

## 🚀 Demo

Check out the live working demo _(if hosted)_ or run it locally using the steps below.

---

## 📂 Project Structure

```
heart_project/
│
├── app.py                    # Flask backend
├── heart_disease_model.pkl   # Trained ML model
├── templates/
│   └── index.html            # Frontend form for input
├── static/
│   └── styles.css (optional) # Add custom styles here
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🧠 Machine Learning Model

The model used is a `DecisionTreeClassifier` trained on a dataset with features like:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Max Heart Rate
- etc.

Model was saved using `joblib` as `heart_disease_model.pkl`.

---

## 📦 Tech Stack

- 🐍 Python
- 🔬 Scikit-learn
- 🧪 Pandas, NumPy
- 🌐 Flask (for the web app)
- 🖥️ HTML/CSS (basic frontend)

---

## ▶️ How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/heart-disease-prediction.git
cd heart-disease-prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📌 Note

- This project is for educational purposes only.
- The predictions made by this model **should not** be used for real medical diagnosis.

---

## 🧑‍💻 Author

- **Your Name**  
- [GitHub Profile](https://github.com/YOUR_USERNAME)

---

## 🌟 Show Some Love

If you found this useful, drop a ⭐ on the repo!
