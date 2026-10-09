SELECT svc_name,
       COUNT(log_id) AS deploy_count
  FROM deploy_logs
  GROUP BY svc_name
  ORDER BY deploy_count DESC;
