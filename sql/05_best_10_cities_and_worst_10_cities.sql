-- Aquí colocaremos 2 consultas, ver las mejores ciudades (mayores sales) y las peores (menores sales)

-- Top 10 mejores sales
SELECT g.city, SUM(s.sales) AS total_sales
FROM sale s
JOIN geography g
ON g.geography_id = s.geography_id
GROUP BY g.city
ORDER BY total_sales DESC
LIMIT 10

-- Top 10 peores sales
SELECT g.city, SUM(s.sales) AS total_sales
FROM sale s
JOIN geography g
ON g.geography_id = s.geography_id
GROUP BY g.city
ORDER BY total_sales ASC
LIMIT 10