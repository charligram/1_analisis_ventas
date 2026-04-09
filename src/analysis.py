import pandas as pd

def create_subcategory_count(df):
    """
    Obtener un DataFrame solo con los datos de cuantos artículos se han vendido por cada categoría

    Args:
        df (pd.DataFrame): DataFrame sin datos nulos con la información necesaria para obtener columna 'Sub-Category'
    
    Returns:
        df_sub_category_count (pd.DataFrame): DataFrame con una columna para la 'Sub-Category' y 
        otra con 'Count' (repetición de cada subcategoria)

    """
    df_sub_category_count = df.groupby('Sub-Category').size()
    df_sub_category_count = df_sub_category_count.reset_index()
    df_sub_category_count = df_sub_category_count.rename(columns={0: 'Count'})
    df_sub_category_count = df_sub_category_count.sort_values('Count', ascending=False)
    return df_sub_category_count

def create_region_total_sale(df):
    """
    Obtener un DataFrame solo con los datos de la región y cuanto dinero ha vendido en total

    Args:
        df (pd.DataFrame): DataFrame sin datos nulos con la información necesaria para obtener columna 'Region'
        y la columna de 'Sales' para sumarla haciendo un total
    
    Returns:
        df_region_total_sale (pd.DataFrame): DataFrame con una columna para la 'Region' y 
        otra con la suma en 'Sales' de cada región

    """
    df_region_total_sale = df.groupby('Region')['Sales'].sum()
    df_region_total_sale = df_region_total_sale.reset_index()
    df_region_total_sale = df_region_total_sale.sort_values('Sales', ascending=False)
    return df_region_total_sale

def create_region_count(df):
    """
    Obtener un DataFrame solo con los datos de cuantos artículos se han vendido en cada región

    Args:
        df (pd.DataFrame): DataFrame sin datos nulos con la información necesaria para obtener columna 'Region'
    
    Returns:
        df_sub_category_count (pd.DataFrame): DataFrame con una columna para la 'Region' y 
        otra con 'Count' (repetición de cada region)

    """
    df_region_count = df.groupby('Region').size()
    df_region_count = df_region_count.reset_index()
    df_region_count = df_region_count.rename(columns={0: 'Count'})
    df_region_count = df_region_count.sort_values('Count', ascending=False)
    return df_region_count

def create_mon_and_tot_sale(df):
    """
    Obtener un DataFrame solo con los datos de fechas separadas por mes y la cantidad vendida en total para ese
    mes en específico

    Args:
        df (pd.DataFrame): DataFrame sin datos nulos con la información necesaria para obtener columna 'Order Date'
        y tambien 'Sales'
    
    Returns:
        df_months_and_total_sale (pd.DataFrame): DataFrame con una columna para cada mes y otra señalando
        cuanto es que se ha vendido en total en ese mes

    """
    df_months_and_total_sale = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    df_months_and_total_sale = df_months_and_total_sale.reset_index()
    df_months_and_total_sale['Order Date'] = df_months_and_total_sale['Order Date'].astype(str)
    df_months_and_total_sale['Order Date'] = pd.to_datetime(df_months_and_total_sale['Order Date'], format='%Y-%m')
    return df_months_and_total_sale

def create_st_and_to_sale(df):
    """
    Calcular y crear cuanto ha vendido (en dinero) en total cada estado. Ademas de guardar el dato de a que región pertenece
    el State.

    Args:
        df (pd.DataFrame): DataFrame sin valores nulos con información de 'State' y 'Sales'.

    Returns:
        df_state_and_total_sale (pd.DataFrame): DataFrame de cuanto ha vendido en total cada estado.
    """
    df_state_and_total_sale = df.groupby(['State', 'Region'])['Sales'].sum()
    df_state_and_total_sale = df_state_and_total_sale.reset_index()
    df_state_and_total_sale = df_state_and_total_sale.sort_values('Sales', ascending=False)
    return df_state_and_total_sale

def create_state_count(df):
    """
    Calcular y crear DataFrame con la cantidad que se ha vendido en cada estado.

    Args:
        df (pd.DataFrame): DataFrame sin valores nulos con información de 'State' para contar su repetición.
    
    Returns:
        df_state_count (pd.DataFrame): DataFrame con la cantidad vendida en cada estado.
    """
    df_state_count = df.groupby('State').size()
    df_state_count = df_state_count.reset_index()
    df_state_count = df_state_count.rename(columns={0: 'Count'}).sort_values('Count', ascending=False)
    return df_state_count