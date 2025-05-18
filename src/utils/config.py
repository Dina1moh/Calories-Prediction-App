# src/utils/config.py
import os
from dotenv import load_dotenv
import joblib

# Load environment variables
load_dotenv()

# App configuration
APP_NAME = os.getenv("APP_NAME", "Customer Churn Prediction")
VERSION = os.getenv("VERSION", "1.0.0")
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "your-secret-key")

# Get the absolute path to the models directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
MODEL_DIR = os.path.join(SRC_DIR, "src", "artifacts")  

# Initialize processor and model as None
preprocessor_X_path = os.path.join(MODEL_DIR, "preprocessor_pridect_calories.joblib")
preprocessor_y_path = os.path.join(MODEL_DIR, "y_pipeline_pridect_calories.joblib")
model_path = os.path.join(MODEL_DIR, "best_model_pridect_calories.joblib")
# Load the preprocessor and model
processor_y = joblib.load(preprocessor_y_path)
processor_X = joblib.load(preprocessor_X_path)
model = joblib.load(model_path)
