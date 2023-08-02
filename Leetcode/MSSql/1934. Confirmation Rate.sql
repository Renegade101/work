WITH totals AS
(SELECT user_id, SUM(CASE WHEN Action = 'confirmed' THEN 1 ELSE 0 END) numerator,
COUNT(*) denominator
FROM Confirmations
GROUP BY user_id)

SELECT su.user_id, ISNULL(ROUND(CAST(numerator AS DECIMAL) / CAST(denominator AS DECIMAL),2),0) AS confirmation_rate
FROM signups AS su
LEFT JOIN totals con ON con.user_id = su.user_id