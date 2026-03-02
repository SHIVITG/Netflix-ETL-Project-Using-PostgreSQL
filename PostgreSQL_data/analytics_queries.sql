-- Example business analytics queries against netflix_final

-- 1. movies vs tv shows distribution
SELECT type, COUNT(*) AS count
FROM netflix_final
GROUP BY type;

-- 2. top 5 countries by number of titles
SELECT country, COUNT(*) AS count
FROM netflix_final
GROUP BY country
ORDER BY COUNT(*) DESC
LIMIT 5;

-- 3. longest movie (duration assumed to be text like '130 min'; may need casting)
SELECT title, duration
FROM netflix_final
WHERE type = 'Movie'
ORDER BY 
    CASE
        WHEN duration ~ '^[0-9]+' THEN CAST(split_part(duration,' ',1) AS INT)
        ELSE 0
    END DESC
LIMIT 1;

-- 4. content classification using violence keywords
SELECT
    CASE
        WHEN description ILIKE '%kill%'
          OR description ILIKE '%violence%'
        THEN 'Bad'
        ELSE 'Good'
    END AS category,
    COUNT(*)
FROM netflix_final
GROUP BY category;

-- add your own queries below
