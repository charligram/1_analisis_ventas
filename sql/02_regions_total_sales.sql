SELECT g.region, SUM(sales) AS total_sales
FROM sale s
JOIN geography g
ON g.geography_id = s.geography_id
GROUP BY g.region
ORDER BY total_sales DESC