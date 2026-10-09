SELECT DISTINCT pod_name 
FROM k8s_pods 
WHERE mem_used > 100 AND mem_used < 500
