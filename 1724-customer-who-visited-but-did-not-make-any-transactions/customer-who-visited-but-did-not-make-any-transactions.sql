# Write your MySQL query statement below
select customer_id, COUNT(*) AS count_no_trans
From Visits AS V
LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY customer_id