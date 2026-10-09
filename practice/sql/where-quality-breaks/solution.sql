-- SELECT * FROM dq_checks LIMIT 5
SELECT tbl_name, 
      AVG(fail_pct) AS avg_fail_pct
FROM dq_checks
GROUP BY tbl_name
HAVING COUNT(rule) > 1
