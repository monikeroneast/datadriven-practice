SELECT ad_campaign, 
       SUM(COALESCE(revenue,0))/ COUNT(impression_id) AS avg_revenue_per_impression
FROM ad_impressions
GROUP BY ad_campaign
ORDER BY avg_revenue_per_impression DESC;
