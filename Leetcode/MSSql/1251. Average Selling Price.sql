SELECT p.product_id, ROUND((SUM(units * price) * 1.0 / SUM(units)), 2) AS average_price 
FROM prices p
JOIN UnitsSold u ON p.product_id = u.product_id
WHERE purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id