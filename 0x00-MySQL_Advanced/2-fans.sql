-- This SQL script selects the origin column, and the sum of fans column as nb_fans,
-- grouped by origin and ordered by nb_fans descending from the 'metal_bands' table.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
