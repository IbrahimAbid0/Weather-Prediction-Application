README for Weather Prediction App
Project Overview
This project is a Weather Prediction Application built using Flask, Streamlit, MLFlow, DVC, and Kubernetes. It uses machine learning to predict humidity levels based on temperature and wind speed. The system is fully containerized using Docker and deployed on Minikube.
Features
Data Collection and Preprocessing: Data is collected using the WeatherStack API, preprocessed, and stored.
Model Training: A Linear Regression model is trained using preprocessed data to predict humidity levels.
Model Versioning: The model is versioned using MLFlow and DVC to ensure reproducibility.
Frontend: A Streamlit application provides an interactive UI for users to input data and get predictions.
Backend: A Flask API handles predictions by receiving requests from the frontend and returning predictions.
Deployment: The application is deployed using Docker and Kubernetes (Minikube) for scalability.

Project Setup and Installation
1. Prerequisites
Before running the project, make sure you have the following installed:
Python 3.9+
Docker
Minikube (for Kubernetes deployment)
MLFlow
DVC
Git
2. Clone the Repository
Clone the repository from GitHub:
git clone https://github.com/your-username/weather-prediction-app.git
cd weather-prediction-app

3. Set Up Virtual Environment
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies
Install the required Python dependencies:
pip install -r requirements.txt

5. Initialize DVC
Initialize DVC to handle dataset and model versioning:
dvc init
dvc remote add -d myremote ./dvc_storage  # Set up local storage for DVC

6. Set Up MLFlow
Run MLFlow locally or configure it to use a remote server:
mlflow ui

This will run the MLFlow UI at http://localhost:5000.
7. Docker Setup
To build and run the Docker images for both the Flask backend and Streamlit frontend:
For the Flask Backend:

 docker build -t flask-backend ./backend
docker run -p 5001:5001 flask-backend


For the Streamlit Frontend:

 docker build -t streamlit-frontend ./frontend
docker run -p 8502:8502 streamlit-frontend


8. Kubernetes Setup (Minikube)
To deploy the app to Minikube:
Start Minikube:

 minikube start


Apply the Kubernetes deployment files for Flask and Streamlit:

 kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/streamlit-deployment.yaml


Access the deployed services:

 minikube service flask-backend-service
minikube service streamlit-frontend-service



Project Workflow
Data Collection: The data is fetched from the WeatherStack API using a Python script (app.py), and stored in CSV format.
Preprocessing: The raw data is cleaned and processed using the script preprocess.py.
Model Training: A Linear Regression model is trained on the processed data using train.py, and the model is logged to MLFlow and versioned using DVC.
Frontend: Users interact with the system through the Streamlit frontend. They input temperature and wind speed, and receive the predicted humidity.
Backend: The Flask API receives requests from the frontend, loads the model from MLFlow, and returns the prediction.

Model Versioning with MLFlow and DVC
MLFlow is used to log model parameters, metrics, and artifacts. The model is versioned and registered in MLFlow for easy retrieval and deployment.
DVC is used to version control datasets and models. The datasets are tracked with DVC, ensuring that they are reproducible and versioned properly.

Troubleshooting
Issue: Model not found in MLFlow.
Solution: Ensure that the model is transitioned to the production stage using the MLFlow client.
Issue: DVC push fails due to missing cache files.
Solution: Re-run dvc add for missing files and dvc push to ensure all files are uploaded to remote storage.


