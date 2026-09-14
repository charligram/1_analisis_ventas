import os                               # Acceso a funcionalidades del sistema operativo desde Python
from dotenv import load_dotenv          # Cargar variables de entorno
from sqlalchemy import create_engine    # Crear motor para conexión a base de datos

# Cargar variables de entorno
load_dotenv()

# Guardar variables
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

# Realizar conexión a base de datos
engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
)