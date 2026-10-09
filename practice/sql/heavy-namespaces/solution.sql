SELECT nspace,
      COUNT(DISTINCT pod_id) AS pod_count
FROM k8s_pods
GROUP BY nspace
HAVING pod_count > 3
