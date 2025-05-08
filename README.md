# Weather Prediction Application

This project is an end-to-end Weather Prediction System that uses machine learning to forecast humidity based on temperature and wind speed. It integrates modern MLOps tools including Flask, Streamlit, MLFlow, DVC, Docker, and Kubernetes (Minikube) to deliver a scalable, reproducible, and interactive web-based solution.

## Features

- Data Collection: Real-time weather data fetched from the WeatherStack API.
- Preprocessing: Cleansing and formatting of raw weather data.
- Model Training: Linear Regression model trained to predict humidity.
- Model Versioning: Tracked and stored with MLFlow and DVC for full reproducibility.
- Frontend: Interactive UI built with Streamlit for user inputs and live predictions.
- Backend: REST API built with Flask to serve predictions.
- Containerization: All components are Dockerized for portability.
- Orchestration: Deployed and managed using Minikube (Kubernetes).

## Tech Stack

| Component        | Tool / Framework     |
|------------------|----------------------|
| ML Framework     | Scikit-learn         |
| Frontend         | Streamlit            |
| Backend          | Flask                |
| Model Tracking   | MLFlow               |
| Data Versioning  | DVC                  |
| Deployment       | Docker, Kubernetes   |
| Data Source      | WeatherStack API     |

## Setup Instructions

### Prerequisites

Ensure the following tools are installed:

- Python 3.9+
- Git
- Docker
- Minikube
- MLFlow
- DVC

### Clone the Repository

```bash
git clone https://github.com/your-username/weather-prediction-app.git
cd weather-prediction-app
```

### Set Up the Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Initialize DVC

```bash
dvc init
dvc remote add -d myremote ./dvc_storage
```

### Launch MLFlow

```bash
mlflow ui
```

Visit the MLFlow UI at: http://localhost:5000

### Build & Run with Docker

#### Backend (Flask API):

```bash
docker build -t flask-backend ./backend
docker run -p 5001:5001 flask-backend
```

#### Frontend (Streamlit):

```bash
docker build -t streamlit-frontend ./frontend
docker run -p 8502:8502 streamlit-frontend
```

### Deploy to Kubernetes with Minikube

```bash
minikube start

kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/streamlit-deployment.yaml

minikube service flask-backend-service
minikube service streamlit-frontend-service
```

## Project Workflow

1. Data Collection:  
   `app.py` collects real-time weather data using the WeatherStack API and stores it as CSV.

2. Preprocessing:  
   `preprocess.py` cleans and standardizes the raw data.

3. Model Training:  
   `train.py` trains a Linear Regression model, logs it to MLFlow, and tracks the dataset using DVC.

4. Frontend (Streamlit):  
   Users input temperature and wind speed; the app returns predicted humidity.

5. Backend (Flask):  
   The API loads the trained model from MLFlow and returns predictions based on input.

## Model Management with MLFlow & DVC

- MLFlow: Tracks model parameters, metrics, and artifacts. Supports model registration and stage transitions.
- DVC: Versions datasets and models to ensure data lineage and reproducibility.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found in MLFlow | Make sure the model is logged and transitioned to Production using MLFlow client. |
| DVC push fails (missing files) | Re-run `dvc add` for the missing files and use `dvc push` to upload to remote. |

## Author

- Ibrahim Abid  
  Roll No: i21-0298  
  BS AI, FAST NUCES Islamabad

## License

This project is open-source and free to use for academic and learning purposes.
