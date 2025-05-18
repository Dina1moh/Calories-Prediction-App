import pandas as pd
from typing import List
from src.utils.schemas import ModelInput, ModelOutput, Prediction_multi_instances_Data
from src.utils.config import processor_X, model, processor_y

def predict_users(users: List[ModelInput]) -> Prediction_multi_instances_Data:
    try:
        df = pd.DataFrame([c.model_dump() for c in users])
        processed_df = processor_X.transform(df)
        predictions_scaled = model.predict(processed_df)
        predictions = processor_y.inverse_transform(predictions_scaled.reshape(-1, 1)).flatten()

        response = [ModelOutput(Calories=float(pred)) for pred in predictions]
        return Prediction_multi_instances_Data(predicted=response)

    except Exception as e:
        raise Exception(f"Error during model prediction: {str(e)}")

