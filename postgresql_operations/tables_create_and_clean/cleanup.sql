-- ==============================================================
-- cleanup.sql: Netflix Titles ETL Transformations
-- Date: March 6, 2026
-- Author: Shivani
-- Class: COMP 3610
-- Description: Applies business rules from ETL_Netflix_Major.xlsx
--              Drops unnecessary columns, converts date_added to DATE, 
--              keeps only required columns for final table.
-- ==============================================================

-- Step 0: Ensure table exists (all TEXT for CSV import)
-- Assume data is already imported into netflix_titles via COPY or pgAdmin import

-- Step 1: Create final clean table with only required columns
DROP TABLE IF EXISTS netflix_titles_final;
CREATE TABLE netflix_titles_final (
    type TEXT,
    title TEXT,
    country TEXT,
    date_added DATE,
    release_year INT,
    rating TEXT,
    duration TEXT
);

-- Step 2: Convert and copy data with business rules applied
INSERT INTO netflix_titles_final (type, title, country, date_added, release_year, rating, duration)
SELECT 
    type,                                    -- Passthrough (object -> TEXT)
    title,                                   -- Passthrough (object -> TEXT)
    country,                                 -- Passthrough (object -> TEXT)
    date_added,                              -- If needed Switch to DATETIME (object -> DATE)
    release_year::INT,                       -- Passthrough (int64 -> INT)
    rating,                                  -- Passthrough (object -> TEXT)
    duration                                 -- Passthrough (object -> TEXT)
FROM netflix_titles
WHERE title IS NOT NULL                     -- Remove null titles (business rule)
  AND date_added IS NOT NULL                -- Remove null dates
;

-- Dropped columns (per business rules): show_id, director, cast_members, duration, listed_in, description

-- Step 3: Verify transformation
SELECT COUNT(*) as row_count FROM netflix_titles;        -- Raw count
SELECT COUNT(*) as final_count FROM netflix_titles_final;   -- Clean count

SELECT * FROM netflix_titles_final 
WHERE date_added IS NULL OR release_year IS NULL 
LIMIT 5;  -- Should return 0 rows (no nulls)

SELECT * FROM netflix_titles_final;

-- Optional: Rename final table to netflix_titles for main use
-- DROP TABLE IF EXISTS netflix_titles;
-- ALTER TABLE netflix_titles_final RENAME TO netflix_titles;



-- ==============================================================
-- Description: Applies business rules from ETL_Netflix_Major.xlsx
--              Filters Netflix=1 only, drops unnecessary columns,
--              renames columns to match final schema.
-- ==============================================================

-- Step 1: Create clean Netflix-only table with required columns only
DROP TABLE IF EXISTS movies_netflix_final;
CREATE TABLE movies_netflix_final (
    title TEXT,                    -- Title -> title (Passthrough)
    release_year INT,              -- Year -> release_year (int64 -> INT)
    target_age_bracket TEXT,       -- Age -> target_age_bracket (Passthrough)
    imdb_rating NUMERIC(3,1),      -- IMDb -> imdb_rating (float64 -> NUMERIC)
    rotten_tomatoes TEXT,          -- Rotten Tomatoes -> rotten_tomatoes (Passthrough)
    country TEXT                   -- Country -> country (Passthrough)
);

-- Step 2: Transform data from movies_all_streaming with business rules (Filter Netflix=1, then drop)
INSERT INTO movies_netflix_final (
    title, release_year, target_age_bracket, imdb_rating, rotten_tomatoes, country
)
SELECT 
    title,                                   -- Passthrough (object -> TEXT)
    year::INT,                               -- Passthrough (int64 -> INT)
    age,                                     -- Passthrough (object -> TEXT)
    imdb::NUMERIC(3,1),                      -- Passthrough (float64 -> NUMERIC(3,1))
    rotten_tomatoes,                       -- Passthrough (object -> TEXT)  
    country                                  -- Passthrough (object -> TEXT)
FROM movies_all_streaming                    -- Source table (not raw)
WHERE netflix = '1'                         -- Filter on Netflix (then drop this column)
  AND title IS NOT NULL                   
;

-- Dropped columns: ID, Hulu, Prime Video, Disney+, Type, Directors, Genres, Language, Runtime

-- Step 3: Verify transformation  
SELECT COUNT(*) as raw_netflix_count FROM movies_all_streaming WHERE netflix = '1';
SELECT COUNT(*) as clean_count FROM movies_netflix_final;

SELECT * FROM movies_netflix_final 
WHERE title IS NULL OR release_year IS NULL 
LIMIT 5;  -- Should return 0 rows


-- ==============================================================
-- Description: Applies business rules from ETL_Netflix_Major.xlsx  
--              Filters Netflix=1 only, drops unnecessary columns,
--              renames columns to match final schema.
-- ==============================================================

-- Step 1: Create clean Netflix-only table with required columns only
DROP TABLE IF EXISTS tv_shows_netflix_final;
CREATE TABLE tv_shows_netflix_final (
    title TEXT,                    -- Title -> title (Passthrough)
    release_year INT,              -- Year -> release_year (int64 -> INT)
    target_age_bracket TEXT,       -- Age -> target_age_bracket (Passthrough)
    imdb_rating NUMERIC(3,1),      -- IMDb -> imdb_rating (float64 -> NUMERIC)
    rotten_tomatoes TEXT           -- Rotten Tomatoes -> rotten_tomatoes (Passthrough)
);

-- Step 2: Transform data from tv_shows_all_streaming with business rules (Filter Netflix=1, then drop)
INSERT INTO tv_shows_netflix_final (
    title, release_year, target_age_bracket, imdb_rating, rotten_tomatoes
)
SELECT 
    title,                                   -- Passthrough (object -> TEXT)
    year::INT,                               -- Passthrough (int64 -> INT)
    age,                                     -- Passthrough (object -> TEXT)
    imdb::NUMERIC(3,1),                      -- Passthrough (float64 -> NUMERIC(3,1))
    rotten_tomatoes                          -- Passthrough (object -> TEXT)
FROM tv_shows_all_streaming                 -- Source table
WHERE netflix = '1'                         -- Filter on Netflix (then drop this column)
  AND title IS NOT NULL
;

-- Dropped columns: ID, Hulu, Prime Video, Disney+, type, Language, Runtime (and others)

-- Step 3: Verify transformation  
SELECT COUNT(*) as raw_netflix_count FROM tv_shows_all_streaming WHERE netflix = '1';
SELECT COUNT(*) as clean_count FROM tv_shows_netflix_final;

SELECT * FROM tv_shows_netflix_final 
WHERE title IS NULL OR release_year IS NULL 
LIMIT 5;  -- Should return 0 rows

-- ==============================================================