def id_name_not_unique(df, col_id, col_name):
    group_id_name = df.groupby(col_id)[col_name].nunique()
    group_id_name_2 = group_id_name[group_id_name > 1]
    return len(group_id_name_2)


def transform_underscore(serie):
    serie_transformed = serie.strip().lower()        # Quitar espacios a los lados y pasar a minúscula
    serie_transformed = serie_transformed.split()    # Separar cada palabra
    serie_transformed = '_'.join(serie_transformed)  # Juntar toda la lista con un '_' entre palabras

    return serie_transformed