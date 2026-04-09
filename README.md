# Proyecto de análisis en Superstore Sales
## Planteamiento del problema
Un hipermercado quiere saber el comportamiento de sus ventas, analizando factores como lo son los productos que mas se venden, en que regiones tienen mas compradores, etc. Todo esto para poder impulsar campañas de marketing en lugares o productos con menos ventas y fidelizar a sectores que generen las mayores ganancias.

## Dataset
Recurso: Kaggle
Registros: 9800
Categorías interesantes:
- Sales
- Order Date
- Region
- State
- Sub-category

## Objetivos
- Detectar comportamiento del mercado a lo largo del tiempo
- Identificar productos que generan mayores ganancias
- Analizar regiones y estados mas contribuyentes

## Limpieza de datos
- Quitar registros con valores nulos en 'Postal Code'
- Transformar columna 'Order Date' a un formato de tiempo

## EDA
### Cantidad vendida por sub-category
Insights:
- Binders y Papers son las categorías que mas se venden
- Posibilidad de mejorar el stock de los productos de esas categorías

### Ventas totales por región
Insights:
- Regiones de 'West' y 'East' son las que mas beneficios traen a la empresa con cierta diferencia
- Las ventas en el sur son pequeñas, podría mejorarse la estrategia de venta

### Cantidad de ventas por región
Insights:
- 'West' y 'East' lideran primer y segundo puesto de mas productos vendidos
- Los gráficos conservan las relaciones con respecto a las ventas, es decir en todas las regiones se compran productos que rondan un precio normal, no se identifica la posibilidad de que en un region se tienda a comprar productos mas caros o mas baratos. Las regiones generan menos porque compran menos cantidad


