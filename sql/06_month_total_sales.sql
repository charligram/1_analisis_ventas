-- Aquí también haremos 2 consultas, una para ver la suma de mes a mes y otra para ver el total completo de cada mes

-- Total mes a mes
SELECT DATE_TRUNC('month', order_date) AS "month", SUM(sales)
FROM sale
GROUP BY "month"
ORDER BY "month"

-- Total del mes completo
SELECT EXTRACT(MONTH FROM order_date) as "month", SUM(sales)
FROM sale
GROUP BY "month"
ORDER BY "month"