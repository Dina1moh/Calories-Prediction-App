# src/utils/controller.py
from flask import Blueprint, request, jsonify, render_template
from src.utils.config import APP_NAME, VERSION
from src.utils.schemas import ModelInput, Prediction_multi_instances_Data
from src.inference import predict_users

controller_bp = Blueprint("controller", __name__)

@controller_bp.route("/", methods=["GET"])
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error rendering template: {str(e)}"

@controller_bp.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]

        inputs = [ModelInput(**item) for item in data]
        response = predict_users(users=inputs)
        return jsonify(response.model_dump())

    except Exception as e:
        return jsonify({"error": str(e)})
