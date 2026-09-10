SELECT EXTRACT(YEAR FROM order_date) AS "year", SUM(saleS)
FROM sale
GROUP BY "year"
ORDER BY "year"