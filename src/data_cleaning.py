import pandas as pd

def clean_na_transform_date(df):
    df = df.dropna(subset=['Postal Code']).copy() # Crear una copia del dataframe original
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
    return df