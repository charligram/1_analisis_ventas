import kagglehub                                # Para descargar datset de kaggle
import pandas as pd                             # Manejar DataFrames
from src.utils import transform_underscore      # Transformar el Product Name a 1 string con "_" en cada separación
from pathlib import Path                        # Manejar rutas

# Definir la raíz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Descargar dataset
dataset_path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
print("Path to dataset files:", dataset_path)

# Leer csv
df = pd.read_csv(Path(dataset_path) / "train.csv")

print(df.head())

# Eliminar registros con Postal Code nulos
df.dropna(subset=['Postal Code'], inplace=True)

# Añadir Product Name al Product ID
df_product_id_name = df[['Product ID', 'Product Name']]

product_name_transformed = df_product_id_name['Product Name'].apply(transform_underscore)

product_id_transformed = df_product_id_name['Product ID'] + '_' + product_name_transformed

df['Product ID'] = product_id_transformed

# Guardar info limpia
CLEAN_DATA_PATH = PROJECT_ROOT / 'data_docker' / 'clean' / 'clean_data.csv'
df.to_csv(CLEAN_DATA_PATH, index=False)