# config/mlflow_config.py

import mlflow

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("Patient_Risk_Stratification")