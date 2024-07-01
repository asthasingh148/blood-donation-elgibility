from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the pre-trained model
model_path = os.path.join('model', 'my_model.joblib')
model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("Received JSON data:", data)
@app.route('/map')
def map_page():
    return render_template('map.html')


    # Extract features from JSON data
    features = [
        data['gender'],
        data['hemoglobinCount'],
        data['age'],
        data['weight'],
        data['underlyingDisease'],
        data['infections'],
        data['medications'],
        data['daysSinceAlcohol'],
        data['bloodDonationFrequency']
    ]

    # Transform features to a format expected by the model
    # Here you might need to encode the categorical variables and scale/normalize numerical features
    # Assuming the model expects numerical values
    prediction = model.predict([features])
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
