# 🧪 Proyecto de análisis en Superstore Sales
## ❓ Planteamiento del problema
Un hipermercado quiere saber el comportamiento de sus ventas, analizando factores como lo son los productos que mas se venden, en que regiones tienen mas compradores, etc. Todo esto para poder impulsar campañas de marketing en lugares/productos con menos ventas y fidelizar a sectores que generen las mayores ganancias.

## ℹ️ Dataset
Recurso: Kaggle

Registros: 9800 

Categorías interesantes:
- Sales
- Order Date
- Region
- State
- Sub-category

## 🎯 Objetivos
- Detectar comportamiento del mercado a lo largo del tiempo
- Identificar productos que generan mayores ganancias
- Analizar regiones y estados mas contribuyentes

## 🧹 Limpieza de datos
- Quitar registros con valores nulos en 'Postal Code'
- Transformar columna 'Order Date' a un formato de tiempo

## 🔎 EDA
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

### Ventas a travez del tiempo
Insights:
- El gráfico muestra una tendencia al alza de las ventas a modo general
- Los períodos entre Enero y Febrero hasta Octube tienden a tener ventas mas bajas
- Los meses de Septiembre y Diciembre siempre tienen un alza importante en las ventas
- En el mes de marzo hay una subida de ventas de manera periódica

### Ventas por estado
Insigths:
- California y New York son los estado con mas ganancias, acumulando entre ambas un 33.4% de las ganancias totales
- En el gráfico de barras, los estado que están desde "Rhode Island" hacia la derecha contribuyen menos del 1% de las ventas cada uno
- Comparando gráficos de cantidad vendida y total de ganancias vendidas, se puede notar que en algunos estados las personas compran productos mas caros que en otros, como por ejemplo lo es "Washington" y "Pennsylvania", en donde en Washington el público compra menos pero genera mayores ganancias, es decir tienden a comprar productos mas caros

## 👁️ Insights claves generales
- Las ventas estan concentradas significativamente en 10-11 estados que son los que aportan mas ganancias, conformando un 71.8% de las ganancias de la superstore
- Los periodos de Septiembre y Diciembre son los mejores para generar ganancias a la superstore, además que esta va en un crecimiento favorable
- Productos con sub-categorias como: Appliances, Labels, Tables, Envelopes, Bookcases, Fasteners, Supplies, Machines, Copiers. No es necesario tener mas de 500 productos disponibles para cada uno en un período de 4 años

## 🏆 Recomendaciones finales
- Analizar capacidad de la superstore para producir los productos. Debido al posible aumento de la demanda en el futuro medianamente cercano.
- Darle prioridad en stock a productos con mayor cantidad de ventas (sobre todo para Binders y Paper)
- Mejorar estrategias de ventas o marketing en estados que pertenezcan a 'South'
- Mantener trabajo realizado en estados como California y New York, mejorar un poco las estrategias en estados como Texas, Washington y Pennsylvania. Ver estrategias de mejora de alto impacto para todo el resto de estados.

## 👤 Autor
Carlos Rojas
