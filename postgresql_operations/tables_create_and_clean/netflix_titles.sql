-- ==============================================================
-- TO DO: Setup and clean netflix_titles table
-- Date: March 3, 2026
-- Author: Shivani
-- Class: COMP 3610
-- Description:
--   1) Recreates the netflix_titles table
--   2) Shows (commented) steps to convert text dates/years
--   3) Changes the postgres user password
-- ==============================================================

-- 1) Drop table if it already exists, then create it fresh
DROP TABLE IF EXISTS netflix_titles;

CREATE TABLE netflix_titles (
    show_id       TEXT,
    type          TEXT,
    title         TEXT,
    director      TEXT,
    cast_members  TEXT,
    country       TEXT,
    date_added    TEXT,
    release_year  TEXT,
    rating        TEXT,
    duration      TEXT,
    listed_in     TEXT,
    description   TEXT
);

-- ==============================================================
-- Section: Clean and update netflix_titles table
-- Note: The following was done last class (Tuesday)
-- ==============================================================

-- The following steps convert the date_added column from text to a proper DATE type, and release_year from text to INT.
-- STEP 1 : Adds a temporary column (date_added_temp) to store cleaned date values.
ALTER TABLE netflix_titles
ADD COLUMN date_added_temp DATE;
-- STEP 2 : Converts existing text-formatted dates into proper DATE values.
UPDATE netflix_titles
SET date_added_temp = TO_DATE(date_added, 'Month DD, YYYY');
-- STEP 3 : Removes the old date_added column stored as text.
ALTER TABLE netflix_titles
DROP COLUMN date_added;
-- STEP 4 : Renames the cleaned temp column back to date_added.
ALTER TABLE netflix_titles
RENAME COLUMN date_added_temp TO date_added;


-- The following steps convert the release_year column from TEXT to a proper INT type.
-- STEP 1 : Adds a temporary column (release_year_temp) to store numeric year values.
ALTER TABLE netflix_titles
ADD COLUMN release_year_temp INT;
-- STEP 2 : Converts existing text-formatted years into integer values.
UPDATE netflix_titles
SET release_year_temp = release_year::INT;
-- STEP 3 : Removes the old release_year column stored as text.
ALTER TABLE netflix_titles
DROP COLUMN release_year;
-- STEP 4 : Renames the cleaned temp column back to release_year.
ALTER TABLE netflix_titles
RENAME COLUMN release_year_temp TO release_year;


-- ==============================================================
-- Section: Change postgres user password
-- ==============================================================

-- Changes the password for the postgres user to 'postgres'. 
-- IN CASE IF WE FORGET PASSWORD, AND FOR CREATING DB CONNECTION WE NEED PASSWORD (NOT RECOMMENDED FOR PRODUCTION ENVIRONMENT).
ALTER USER postgres WITH PASSWORD 'postgres';
