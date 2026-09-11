SELECT p.subcategory, SUM(sales) AS total_sales
FROM sale s
JOIN product p
ON p.product_id = s.product_id
GROUP BY p.subcategory
ORDER BY total_sales DESC
LIMIT 10