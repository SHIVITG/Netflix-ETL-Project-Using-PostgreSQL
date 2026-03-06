-- ==============================================================
-- Author: Shivani
-- Date: March 6, 2026
-- Description:
-- Master script to build the final integrated Netflix dataset.
-- This script assumes raw tables are already imported.
-- ==============================================================


-- ==============================================================
-- STEP 1: Drop previous final table
-- ==============================================================

DROP TABLE IF EXISTS netflix_final;

-- ==============================================================
-- STEP 2: Create integrated table
-- ==============================================================

CREATE TABLE netflix_final AS
SELECT
    nt.title,
    nt.type,
    nt.release_year,
    nt.country,
    nt.rating,
    nt.duration,
    COALESCE(ma.imdb_rating, ta.imdb_rating) AS imdb,
    COALESCE(ma.rotten_tomatoes, ta.rotten_tomatoes) AS rotten_tomatoes,
	COALESCE(ma.target_age_bracket, ta.target_age_bracket) AS target_age_bracket

FROM netflix_titles_final nt

LEFT JOIN movies_netflix_final ma
    ON LOWER(TRIM(nt.title)) = LOWER(TRIM(ma.title))
    AND nt.release_year = ma.release_year

LEFT JOIN tv_shows_netflix_final ta
    ON LOWER(TRIM(nt.title)) = LOWER(TRIM(ta.title))
    AND nt.release_year = ta.release_year;


-- ==============================================================
-- STEP 3: Create indexes for performance
-- ==============================================================

CREATE INDEX idx_netflix_final_type
ON netflix_final(type);

CREATE INDEX idx_netflix_final_year
ON netflix_final(release_year);

CREATE INDEX idx_netflix_final_country
ON netflix_final(country);

CREATE INDEX idx_netflix_title_year
ON netflix_titles(title, release_year);

-- ==============================================================
-- STEP 4: Verification
-- ==============================================================

-- Total rows in final dataset
SELECT COUNT(*) AS final_row_count
FROM netflix_final;


-- Check for missing titles
SELECT *
FROM netflix_final
WHERE title IS NULL
LIMIT 5;


-- Preview results
SELECT *
FROM netflix_final
LIMIT 20;


-- Count movies vs TV shows
SELECT type, COUNT(*)
FROM netflix_final
GROUP BY type;

-- Check missing ratings
SELECT *
FROM netflix_final
WHERE imdb IS NULL
LIMIT 10;