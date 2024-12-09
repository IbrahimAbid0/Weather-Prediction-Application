from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pandas as pd

app = Flask(__name__)

# Load the model
model_uri = "models:/weather-prediction-model-new/latest"  # Use the production stage
model = mlflow.sklearn.load_model(model_uri)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    temperature = data["temperature"]
    wind_speed = data["wind_speed"]

    input_data = pd.DataFrame({"Temperature": [temperature], "Wind Speed": [wind_speed]})
    prediction = model.predict(input_data)

    return jsonify({"predicted_humidity": prediction[0]})

if __name__ == "__main__":
    # Run Flask on a different port (e.g., 5001)
    app.run(debug=True, port=5001)  # Flask will now run on http://localhost:5001
