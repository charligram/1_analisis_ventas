import pandas as pd  # Manejar DataFrames
import numpy as np

# Detalle: Las columnas que se utilicen en las funciones deben ser las columnas con la sintáxis de la BD porque de ahí se recupera la info.


def get_weekly_sales(engine):
    """
    Devuelve las ventas semanales sumadas, desde la base de datos.

    Args:
        engine: Conexión a la base de datos

    Returns:
        df_week_sales (pd.DataFrame): DataFrame con ventas semanales totales en cada registro
    """

    query = """
    SELECT order_date, sales
    FROM sale
    ORDER BY sales ASC
    """

    df = pd.read_sql(query, engine)

    df['order_date'] = pd.to_datetime(df['order_date'])

    df_week_sales = df.groupby(pd.Grouper(key='order_date', freq='W'))['sales'].sum().reset_index()

    return df_week_sales



def create_features(df_week_sales):
    """
    Crear features de lags, rolling, month/year a partir del DataFrame con las ventas semanales.

    Args:
        df_week_sales (pd.DataFrame): DataFrame con ventas agrupadas por semana. Debe incluir columnas 'order_date' y 'sales'

    Returns:
        df_week_sales: DataFrame enriquecido con lags, rolling, mes y año para cada semana.
    """

    # Lags
    weeks_of_lag = ['1', '2', '3', '4']

    for lag in weeks_of_lag:
        df_week_sales[f'Lag_{lag}'] = df_week_sales['sales'].shift(int(lag))

    # Rolling
    df_week_sales['Rolling_4'] = df_week_sales['sales'].shift(1).rolling(4).mean()

    # Month and Year
    df_week_sales['Month'] = df_week_sales['order_date'].dt.month
    df_week_sales['Year'] = df_week_sales['order_date'].dt.year

    return df_week_sales



def forecast_prediction(df_week_sales, model, weeks_to_predict):
    """
    Realizar predicciones para X semanas hacia delante a partir de la última fecha registrada.

    Args:
        df_week_sales (pd.DataFrame): DataFrame con las ventas semanales totales, incluyendo los lags, rolling, month y year para cada registro.
            Debe contener los features de: 'order_date', 'lag_1', 'lag_2', 'lag_3', 'lag_4', 'rolling_4', 'month', 'year 
        model: Modelo entrenado listo para realizar predicciones.
        weeks_to_predict (int): Número de semanas proximas a predecir.

    Returns:
        df_predictions (pd.DataFrame): DataFrame con fechas y predicciones de ventas para cada semana.
    """

    # Lista donde guardaremos las siguientes X semanas
    predictions = []

    # Historial de ventas
    history_sales = list(df_week_sales['sales'])

    # Obtener último día registrado
    last_date = df_week_sales['order_date'].iloc[-1]

    for i in range(1, weeks_to_predict+1):

        # Crear lags para la predicción
        lag_1 = [history_sales[-1]]
        lag_2 = [history_sales[-2]]
        lag_3 = [history_sales[-3]]
        lag_4 = [history_sales[-4]]

        # Crear rolling
        rolling_4 = [np.mean(history_sales[-4:])]

        # Obtener mes y año
        next_date = last_date + pd.Timedelta(weeks=i)       # Sumarle al último dia, i semanas más

        month = next_date.month
        year = next_date.year

        # Crear DataFrame para la predicción
        x_to_predict = pd.DataFrame({
            'Lag_1': lag_1,
            'Lag_2': lag_2,
            'Lag_3': lag_3,
            'Lag_4': lag_4,
            'Rolling_4': rolling_4,
            'Month': month,
            'Year': year
        })

        # Generar predicción
        y_pred = model.predict(x_to_predict)[0]

        # Agregar la predicción a la lista del historial (para que el proceso se haga todo de nuevo con la predicción como información)
        history_sales.append(y_pred)

        # Agrgar predicciones a la lista
        predictions.append({
            'order_date': next_date,
            'sales': y_pred
        })

    # Finalmente convertir las predicciones en un DataFrame y retornar
    df_predictions = pd.DataFrame(predictions)

    return df_predictions

