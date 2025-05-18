# src/utils/schemas.py
from pydantic import BaseModel, Field
from typing import List

class ModelInput(BaseModel):
    Gender: str = Field(..., description="Gender of the user: 'Male' or 'Female'")
    Age: int = Field(..., ge=0)
    Height: float = Field(..., ge=0)
    Weight: float = Field(..., ge=0)
    Duration: float = Field(..., ge=0)
    Heart_Rate: float = Field(..., ge=0)
    Body_Temp: float = Field(..., ge=0)

class ModelOutput(BaseModel):
    Calories: float = Field(..., ge=0)

class Prediction_multi_instances_Data(BaseModel):
    predicted: List[ModelOutput]
