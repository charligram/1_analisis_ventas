from pydantic import BaseModel

class PredictionInput(BaseModel):
    weeks_to_predict: int