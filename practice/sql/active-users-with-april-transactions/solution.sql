SELECT COUNT(DISTINCT u.user_id) AS active_users_with_transactions
FROM users u
INNER JOIN transactions t 
ON 
u.user_id = t.user_id
WHERE t.transaction_date >= '2026-04-01' AND 
      t.transaction_date < '2026-05-01' AND
      u.account_status = 'active'
