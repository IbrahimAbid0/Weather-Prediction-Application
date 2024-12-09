from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import pandas as pd

# Load the preprocessed data
df = pd.read_csv("processed_data.csv")

# Split data into features and target
X = df[["Temperature", "Wind Speed"]]
y = df["Humidity"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model MSE: {mse}")

experiment_name = "weather-prediction-experiment-new"
mlflow.set_experiment(experiment_name)

# Start an MLFlow run to log the model and metrics
with mlflow.start_run() as run:
    # Log model parameters
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)

    # Log the model's performance metrics
    mlflow.log_metric("mse", mse)

    # Log the trained model
    mlflow.sklearn.log_model(model, "model")

    print(f"Model and metrics logged to MLFlow (Run ID: {run.info.run_id})")

    # Register the model in MLFlow's Model Registry
    model_name = "weather-prediction-model-new"
    model_uri = f"runs:/{run.info.run_id}/model"
    
    # Register the model in the registry (only once)
    mlflow.register_model(model_uri, model_name)
    print(f"Model registered with name: {model_name}")

# # Initialize the MLFlow client
# client = MlflowClient()

# # Assign the model to the 'production' stage
# model_name = "weather-prediction-model"
# model_version = 1  # Use the appropriate version you registered (e.g., version 1)

# # Transition the model version to 'production'
# client.transition_model_version_stage(
#     name=model_name,
#     version=model_version,
#     stage="Production"
# )

# print(f"Model version {model_version} moved to 'production' stage.")

# Load the registered model by its name (use "production" stage or "latest" version)
model_uri = "models:/weather-prediction-model/latest"
model = mlflow.sklearn.load_model(model_uri)
# model = mlflow.sklearn.load_model(model_uri)

# Example usage of the loaded model to make predictions
input_data = pd.DataFrame({"Temperature": [25], "Wind Speed": [10]})
prediction = model.predict(input_data)
print(f"Predicted Humidity: {prediction[0]:.2f}%")

# Save the model using MLFlow
mlflow.sklearn.log_model(model, "model")

# Alternatively, save it manually with pickle or joblib
import joblib
joblib.dump(model, 'model.pkl')