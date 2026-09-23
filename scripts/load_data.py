from pathlib import Path                # Manejar rutas
import pandas as pd                     # Manejar DataFrames
import os
from sqlalchemy import create_engine    # Crear engine para conectar al servicio de bases de datos postgres

# Ruta raíz
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Obtener información limpia
clean_data_path = PROJECT_ROOT / 'data_docker' / 'clean' / 'clean_data.csv'

df = pd.read_csv(clean_data_path)
print(df.head())


# Cambiar 'Order Date' a datetime para ordenar la información
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')

df = df.sort_values(by='Order Date', ascending=True)


# Eliminar 'Row ID' y resetear índice
df = df.drop(columns=['Row ID'])

df.reset_index(inplace=True, drop=True)


# Obtener cada producto diferente
df_products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']].drop_duplicates()

# Cambiar nombres de las columnas para que coincidan con las de la base de datos.
df_products.columns = [
    'product_id',
    'product_name',
    'category',
    'subcategory'
]
df_products.head()

# Obtener cada geografía diferente
df_geography = df[['Country', 'City', 'State', 'Region', 'Postal Code']].drop_duplicates()
df_geography.head()

# Cambiar nombres para la base de datos.
df_geography.columns = [
    'country',
    'city',
    'state',
    'region',
    'postal_code'
]
# Considerar que aquí nos estaría faltando el id de cada geography



# Obtener cada cliente (customer)
df_customers = df[['Customer ID', 'Customer Name']].drop_duplicates()
df_customers.head()

# Cambiar nombres de columnas.
df_customers.columns = ['customer_id', 'customer_name']
df_customers.head()


# Obtener sales data
df_sales = df[['Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Segment', 'Product ID', 'Customer ID', 'Country', 'City', 'State', 'Region', 'Postal Code', 'Sales']].drop_duplicates()
df_sales.head()

# Cambiar nombres de columnas.
df_sales.columns = ['order_id', 'order_date', 'ship_date', 'ship_mode', 'segment', 'product_id', 'customer_id', 'country', 'city', 'state', 'region', 'postal_code', 'sales']
df_sales.head()


# Obtener y guardar las variables de entorno para la conexión
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

print(f'User: {user}\nHost: {host}\nPort: {port}\nDatabase: {database}')

# Conexión a la base de datos.
engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
)

# Cargar data en la base de datos
# Productos
df_products.to_sql(
    'product',
    engine,
    if_exists='append',
    index=False
)

# Geography
df_geography.to_sql(
    'geography',
    engine,
    if_exists='append',
    index=False
)

# Customer
df_customers.to_sql(
    'customer',
    engine,
    if_exists='append',
    index=False
)

# Cargar sales
# Primero obtener los id's de cada geography, para poder asignarlo a sales
geography_db = pd.read_sql(
    """
    SELECT * FROM geography
    """,
    engine
)


# Mergear info
df_sales['postal_code'] = df_sales['postal_code'].astype(str)       # Cambiar type de postal_code

df_sales = df_sales.merge(
    geography_db,
    on=['country', 'city', 'state', 'region', 'postal_code'],
    how='left'
)

df_sales.head()

# Añadir sales a la base de datos
# Eliminamos los features que corresponden a geography
df_sales.drop(columns=['country', 'city', 'state', 'region', 'postal_code'], inplace=True)

# Ordenar DataFrame
df_sales = df_sales[[
    'order_id',
    'order_date',
    'ship_date',
    'ship_mode',
    'segment',
    'product_id',
    'geography_id',
    'customer_id',
    'sales'
]]

df_sales.to_sql(
    'sale',
    engine,
    if_exists='append',
    index=False
)