SELECT 
  CAST(deploy_at AS DATE) AS deploy_date,
  COUNT(log_id) AS deploy_count
FROM deploy_logs
GROUP BY deploy_date
ORDER BY deploy_date;
