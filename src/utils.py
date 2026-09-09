def id_name_not_unique(df, col_id, col_name):
    group_id_name = df.groupby(col_id)[col_name].nunique()
    group_id_name_2 = group_id_name[group_id_name > 1]
    return len(group_id_name_2)