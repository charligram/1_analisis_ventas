import os                                            # Acceso a funcionalidades del sistema operativo desde Python
from dotenv import load_dotenv, find_dotenv          # Cargar variables de entorno/Encontrar variables de entorno
from sqlalchemy import create_engine                 # Crear motor para conexión a base de datos

# Como Docker de por sí carga las variables de entorno cuando se levanta el contenedor, primero veremos si cargo la variable
# RUNNING_IN_DOCKER, de ser así, simplemente ocupamos las variables. En caso contrario, cargaremos las variables del .env.local
# ya que significaría que el proyecto se está corriendo de forma manual
if not os.getenv('RUNNING_IN_DOCKER'):
    load_dotenv(find_dotenv('.env.local'), override=True)

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