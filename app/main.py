from fastapi import FastAPI
from app.services.database_connection import engine
from app.services.prediction import get_weekly_sales, create_features, forecast_prediction
from app.schemas.predict import PredictionInput, PredictionOutput
import joblib


# App
app = FastAPI()

# Cargar modelo XGBoost
xgboost_model = joblib.load('models/xgboost_model.pkl')

# Raíz
@app.get("/")                           # Cuando alguien hace una petición get a "/", se ejecuta la funcion de abajo
def root():                             # Función disparada por la solicitud get
    return {'message': 'API Works'}     # Cuerpo de la función

# Endpoint de predicciones
# Añadir data: PredictionInput hace que se tenga que cargar como argumento lo indicado en el schema (los atributos quedan guardados en data)
# Añadir response_model=list[PredictionOutput] permite señalar que lo que se debe devolver es una lista con objetos tipo PredictionOutput, es decir que tengan order_date y sales
@app.post("/predict", response_model=list[PredictionOutput])
def predict(data: PredictionInput):

    # Obtener DataFrame con ventas totales por semana
    df_weekly_sales = get_weekly_sales(engine)

    # Crear features
    df_weekly_sales = create_features(df_weekly_sales)

    # Realizar predicciones (data contiene los valores ingresados para la predicción)
    df_predictions = forecast_prediction(df_weekly_sales, xgboost_model, data.weeks_to_predict)

    # Devolver predicciones en forma de diccionario (orient='records' hace que cada registro sea un diccionario) 
    return df_predictions.to_dict(orient='records')
