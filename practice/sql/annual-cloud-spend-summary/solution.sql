SELECT 
      EXTRACT(YEAR FROM CAST(bill_date AS DATE)) AS fiscal_year,
      SUM(amount) AS total_spend,
      COUNT(DISTINCT svc_name) AS service_count
FROM cloud_costs
GROUP BY fiscal_year
ORDER BY fiscal_year DESC;
