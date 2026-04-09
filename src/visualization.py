import plotly.graph_objects as go

def create_fig_subca_count(df_sub_category_count):
    """
    Crear figure con la cantidad de compras por subcategoria.

    Args:
        df_sub_category_count (pd.DataFrame): Datos ya creados con columnas de Sub-Category y su repeticion en el DataFrame.
    
    Returns:
        fig_sub_category_count (go.Figure): Figure comparando las subcategorias y cantidad comprada en total.
    """
    fig_sub_category_count = go.Figure()
    fig_sub_category_count.add_trace(
        go.Bar(
            x=df_sub_category_count['Sub-Category'],
            y=df_sub_category_count['Count']
        )
    )
    fig_sub_category_count.update_layout(
        title='Cantidad comprada por sub-categoria',
        xaxis=dict(title='Sub-categoria'),
        yaxis=dict(title='Cantidad de compras')
    )
    return fig_sub_category_count

def create_fig_re_to_sa(df_region_total_sale):
    """
    Crear figure con la suma del "Sale" para cada región.

    Args:
        df_region_total_sale (pd.DataFrame): Datos ya creados con columnas de region y su total de ventas.
    
    Returns:
        fig_region_total_sale (go.Figure): Figure comparando cada region con la venta total hasta el momento.
    """
    fig_region_total_sale = go.Figure()
    fig_region_total_sale.add_trace(
        go.Bar(
            x=df_region_total_sale['Region'],
            y=df_region_total_sale['Sales']
        )
    )

    fig_region_total_sale.update_layout(
        title='Ventas totales por región',
        xaxis=dict(title='Regiones'),
        yaxis=dict(title='Total vendido')
    )
    return fig_region_total_sale

def create_fig_region_count(df_region_count):
    """
    Crear figure con la cantidad de compras que se han hecho en cada región.

    Args:
        df_region_count (pd.DataFrame): Datos ya creados con columnas de region y la cantidad de compras que se han hecho en ella.
    
    Returns:
        fig_region_count (go.Figure): Figure comparando cada region con la cantidad de artículos que ha vendido.
    """
    fig_region_count = go.Figure()
    fig_region_count.add_trace(
        go.Bar(
            x=df_region_count['Region'],
            y=df_region_count['Count']
        )
    )

    fig_region_count.update_layout(
        title='Cantidades vendidas por región',
        xaxis=dict(title='Regiones'),
        yaxis=dict(title='Cantidad vendida')
        )
    return fig_region_count

def create_m_and_ts(df_months_and_total_sale):
    """
    Crear figure mostrando como se comportan las ventas a medida que ha pasado el tiempo.

    Args:
        df_months_and_total_sale (pd.DataFrame): DataFrame que contiene solo 2 columnas, la primera indica cada mes
        y la segunda la venta total que se ha hecho en ese mes.

    Returns:
        fig_months_total_sale (go.Figure): Figure de lineas mostrando ventas totales por meses
    """
    fig_months_total_sale = go.Figure()
    fig_months_total_sale.add_trace(
        go.Scatter(
            mode='lines',
            x=df_months_and_total_sale['Order Date'],
            y=df_months_and_total_sale['Sales']
        )
    )

    fig_months_total_sale.update_layout(
        title='Comportamiento de ventas por mes',
        xaxis=dict(title='Fechas'),
        yaxis=dict(title='Ventas')
    )
    return fig_months_total_sale

def create_fig_st_and_to_sale(df_state_and_total_sale):
    """
    Crear figure con diagrama de barras comparando cuanto ha vendido cada estado.

    Args:
        df_state_and_total_sale (pd.DataFrame): DataFrame que contiene en cada registro el estado y cuanto ha
        vendido en precio.
    
    Returns:
        fig_state_and_total_sale (go.Figure): Figure con lo que ha vendido cada estado en total.
    """

    # En este bloque es necesario mapear cada color por region, es decir en la columna region cada vez que encuentra una de
    # las opciones la reemplaza por el color indicado
    region_colors = {
        'West': '#1f77b4',
        'East': '#ff7f0e',
        'Central': '#2ca02c',
        'South': '#d62728'
    }
    bar_colors = df_state_and_total_sale['Region'].map(region_colors)

    fig_state_and_total_sale = go.Figure()
    fig_state_and_total_sale.add_trace(
        go.Bar(
            x=df_state_and_total_sale['State'],
            y=df_state_and_total_sale['Sales'],
            marker=dict(color=bar_colors)
        )
    )

    fig_state_and_total_sale.update_layout(
        title='Ventas totales por estado',
        xaxis=dict(title='Estados'),
        yaxis=dict(title='Ventas')
    )
    return fig_state_and_total_sale

def create_fig_st_and_to_sale_pie(df_state_and_total_sale):
    """
    Crear figure con gráfico de pie dsitribuyendo cuanto ha vendido cada estado.

    Args:
        df_state_and_total_sale (pd.DataFrame): DataFrame que contiene en cada registro el estado y cuanto ha
        vendido en precio.
    
    Returns:
        fig_state_and_total_sale_pie (go.Figure): Figure con lo que ha vendido cada estado en total en forma de pie.
    """
    fig_state_and_total_sale_pie = go.Figure()
    fig_state_and_total_sale_pie.add_trace(
        go.Pie(
            labels=df_state_and_total_sale['State'],
            values=df_state_and_total_sale['Sales']
        )
    )
    return fig_state_and_total_sale_pie


def create_fig_state_count(df_state_count):
    """
    Crear figure de barras comparando la cantidad que se ha vendido en cada estado.

    Args:
        df_state_count (pd.DataFrame): DataFrame con solo las columnas del estado y cuanto ha vendido ese estado en cantidad.
    
    Returns:
        fig_state_count (go.Figure): Figure de grafico de barras con los estados y cantidad vendida.
    """
    fig_state_count = go.Figure()
    fig_state_count.add_trace(
        go.Bar(
            x=df_state_count['State'],
            y=df_state_count['Count']
        )
    )

    fig_state_count.update_layout(
        title='Cantidad de ventas por estado',
        xaxis=dict(title='Estado'),
        yaxis=dict(title='Cantidad de ventas')
    )
    return fig_state_count