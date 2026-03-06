-- ==============================================================
-- analysis.sql: Netflix Final Table Analytics
-- Author: Shivani Tyagi
-- Class: COMP 3610
-- Description:
-- This script contains queries to answer analytical questions
-- from the integrated Netflix dataset.
-- Can later be used for Python integration / Streamlit app.
-- ==============================================================

-- ==============================================================
-- Question 1: Top 10 Netflix movies by IMDb rating
-- ==============================================================

SELECT title, release_year, imdb, country
FROM netflix_final
WHERE type = 'Movie' AND imdb IS NOT NULL
ORDER BY imdb DESC
LIMIT 10;


-- ==============================================================
-- Question 2: Top 10 Netflix TV Shows by IMDb rating
-- ==============================================================

SELECT title, release_year, imdb, country
FROM netflix_final
WHERE type = 'TV Show' AND imdb IS NOT NULL
ORDER BY imdb DESC
LIMIT 10;


-- ==============================================================
-- Question 3: Distribution of Netflix content by country
-- ==============================================================

SELECT country, COUNT(*) AS content_count
FROM netflix_final
GROUP BY country
ORDER BY content_count DESC;


-- ==============================================================
-- Question 4: Content count by target age bracket
-- ==============================================================

SELECT target_age_bracket, COUNT(*) AS count
FROM netflix_final
GROUP BY target_age_bracket
ORDER BY count DESC;


-- ==============================================================
-- Question 5: Rating distribution (Netflix rating vs IMDb)
-- ==============================================================

SELECT rating, COUNT(*) AS count
FROM netflix_final
GROUP BY rating
ORDER BY count DESC;

SELECT CASE 
           WHEN imdb >= 8 THEN 'Excellent'
           WHEN imdb >= 6 THEN 'Good'
           WHEN imdb >= 4 THEN 'Average'
           ELSE 'Poor'
       END AS imdb_category,
       COUNT(*) AS count
FROM netflix_final
WHERE imdb IS NOT NULL
GROUP BY imdb_category
ORDER BY count DESC;


-- ==============================================================
-- Question 6: Cross-analysis - Movies vs TV Shows per country
-- ==============================================================

SELECT country, type, COUNT(*) AS count
FROM netflix_final
GROUP BY country, type
ORDER BY country, type;