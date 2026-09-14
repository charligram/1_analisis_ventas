from fastapi import FastAPI

app = FastAPI()


@app.get("/")                           # Cuando alguien hace una petición get a "/", se ejecuta la funcion de abajo
def root():                             # Función disparada por la solicitud get
    return {'message': 'API Works'}     # Cuerpo de la función