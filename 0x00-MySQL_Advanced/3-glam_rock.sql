-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       IF(lifespan_split[1] = 0, 2022 - lifespan_split[0], lifespan_split[1] - lifespan_split[0]) AS lifespan
FROM (
    SELECT band_name, 
           SPLIT_STRING(lifespan, '-') AS lifespan_split
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', main_style) > 0
) AS glam_bands
ORDER BY lifespan DESC;
