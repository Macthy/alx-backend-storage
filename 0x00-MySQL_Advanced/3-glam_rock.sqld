-- List Glam rock bands ranked by longevity
SELECT band_name, IF(splits IS NULL, 2022 - formed, 2022 - MAX(splits)) AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;

