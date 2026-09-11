SELECT p.category, SUM(sales) AS total_sales
FROM sale s
JOIN product p
ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY total_sales DESC