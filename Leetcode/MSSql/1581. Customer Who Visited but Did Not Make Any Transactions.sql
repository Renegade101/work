SELECT customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits V LEFT JOIN Transactions T ON V.visit_id = T.visit_id
WHERE T.visit_id IS Null
GROUP BY customer_id
