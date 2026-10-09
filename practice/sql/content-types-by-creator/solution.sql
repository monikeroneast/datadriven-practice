-- SELECT * FROM content_items LIMIT 5
SELECT DISTINCT content_type
FROM content_items 
WHERE creator_id = 100
