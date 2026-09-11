def id_name_not_unique(df, col_id, col_name):
    """
    Cuenta la cantidad de filas que tienen un id asignado a mas de 1 nombre (inconsistencia).

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas a revisar.
        col_id (str): Nombre de la columna que contiene los id's.
        col_name (str): Nombre de la columna que contiene los nombres.

    Returns
        (int): Número de filas con más de 1 nombre por id.
    """
    group_id_name = df.groupby(col_id)[col_name].nunique()
    group_id_name_2 = group_id_name[group_id_name > 1]
    return len(group_id_name_2)


def transform_underscore(serie):
    """
    Retorna la serie que fue ingresada con underscore's entre cada palabra de cada registro.

    Args:
        serie (pd.Serie): Serie la cual se quiere transformar.

    Returns:
        serie (pd.Serie): Serie transformada con underscores
    """
    serie_transformed = serie.strip().lower()        # Quitar espacios a los lados y pasar a minúscula
    serie_transformed = serie_transformed.split()    # Separar cada palabra
    serie_transformed = '_'.join(serie_transformed)  # Juntar toda la lista con un '_' entre palabras

    return serie_transformed