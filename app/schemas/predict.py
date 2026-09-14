from pydantic import BaseModel
from datetime import date

class PredictionInput(BaseModel):
    weeks_to_predict: int

class PredictionOutput(BaseModel):
    order_date: date
    sales: float