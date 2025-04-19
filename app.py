from flask import Flask, jsonify, request, send_from_directory
import pickle
import numpy as np
import traceback

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("heart_disease_model.pkl", "rb"))

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract features from the form data
        features = np.array([
            data['age'],
            1 if data['sex'] == 'Male' else 0,
            1 if data['chest_pain_type'] == 'Typical angina' else 0,
            data['resting_blood_pressure'],
            data['cholestoral'],
            1 if data['fasting_blood_sugar'] == 'Greater than 120 mg/ml' else 0,
            1 if data['rest_ecg'] == 'ST-T wave abnormality' else 0,
            data['Max_heart_rate'],
            1 if data['exercise_induced_angina'] == 'Yes' else 0,
            data['oldpeak'],
            1 if data['slope'] == 'Downsloping' else (0 if data['slope'] == 'Flat' else -1),
            data['vessels_colored_by_flourosopy'],
            1 if data['thalassemia'] == 'Reversable Defect' else (0 if data['thalassemia'] == 'Normal' else -1)
        ])

        # Reshape to match the model input
        features = features.reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        # Log error details for debugging
        print("Error occurred during prediction:", str(e))
        print("Stack trace:", traceback.format_exc())
        return jsonify({'error': 'Error predicting result'}), 500

if __name__ == '__main__':
    app.run(debug=True)