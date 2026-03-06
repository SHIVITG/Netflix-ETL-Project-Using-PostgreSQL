-- ==============================================================
-- TO DO: Setup and clean movies_all_streaming table
-- Date: March 6, 2026
-- Author: Shivani
-- Class: COMP 3610
-- Description:
--   1) Recreates the movies_all_streaming table
--   2) (Optional) Converts text/numeric columns to proper data types
-- ==============================================================

-- 1) Drop table if it already exists, then create it fresh
DROP TABLE IF EXISTS movies_all_streaming;

-- movies_all_streaming: all columns as TEXT for easy CSV import
-- pre‑clean the CSV (for example, in Excel delete the first unnamed column, 
-- or with a tool like cut in Linux) so the first column is ID instead of the index, 
-- then import normally with CSV HEADER.

CREATE TABLE movies_all_streaming (
    id              INT,
    title           TEXT,
    year            INT,
    age             TEXT,
    imdb            NUMERIC(3,1),
    rotten_tomatoes TEXT,
    netflix         INT,
    hulu            INT,
    prime_video     INT,
    disney_plus     INT,
    type            INT,
    directors       TEXT,
    genres          TEXT,
    country         TEXT,
    language        TEXT,
    runtime         INT
);

-- Shows all rows and columns in the movies_all_streaming table.
SELECT * FROM movies_all_streaming;

-- ==============================================================
-- Section: Clean and update movies_all_streaming table
-- Note: Use these kinds of steps after loading raw CSV data.
-- ==============================================================

-- Example: If YEAR came in as TEXT, convert it to INT (similar to release_year before).

-- The following steps convert the year column from TEXT to a proper INT type.

-- STEP 1 : Adds a temporary column (year_temp) to store numeric year values.
-- ALTER TABLE movies_all_streaming
-- ADD COLUMN year_temp INT;

-- STEP 2 : Converts existing text-formatted years into integer values.
-- UPDATE movies_all_streaming
-- SET year_temp = year::INT;

-- STEP 3 : Removes the old year column stored as text.
-- ALTER TABLE movies_all_streaming
-- DROP COLUMN year;

-- STEP 4 : Renames the cleaned temp column back to year.
-- ALTER TABLE movies_all_streaming
-- RENAME COLUMN year_temp TO year;

-- Example: If runtime was text, you could do the same pattern to convert to INT.

-- SELECT * FROM movies_all_streaming;
-- Shows all rows and columns in the movies_all_streaming table.

