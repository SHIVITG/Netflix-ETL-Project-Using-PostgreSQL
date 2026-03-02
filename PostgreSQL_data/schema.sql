-- PostgreSQL schema definition for Netflix ETL Project
-- Run this file from psql after creating the database

--
-- 1. create database (if you have permission)
--    createdb AreYouStillWatching_db
--    \c AreYouStillWatching_db
--

-- 2. create raw tables

DROP TABLE IF EXISTS netflix_titles;
CREATE TABLE netflix_titles (
    show_id TEXT,
    type TEXT,
    title TEXT,
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added DATE,
    release_year INT,
    rating TEXT,
    duration TEXT,
    listed_in TEXT,
    description TEXT
);

DROP TABLE IF EXISTS movies_all_streaming;
CREATE TABLE movies_all_streaming (
    id INT,
    title TEXT,
    year INT,
    age TEXT,
    imdb FLOAT,
    rotten_tomatoes TEXT,
    netflix INT,
    hulu INT,
    prime_video INT,
    disney_plus INT
);

DROP TABLE IF EXISTS tv_shows_all_streaming;
CREATE TABLE tv_shows_all_streaming (
    id INT,
    title TEXT,
    year INT,
    age TEXT,
    imdb FLOAT,
    rotten_tomatoes TEXT,
    netflix INT,
    hulu INT,
    prime_video INT,
    disney_plus INT
);

-- 3. load raw CSV data using COPY (paths are relative to server process)
--    adjust the path to your workspace location or use \copy from client
--
-- Example:
-- \copy netflix_titles FROM '/full/path/to/Raw_Data/netflix_titles.csv' WITH CSV HEADER;
-- \copy movies_all_streaming FROM '/full/path/to/Raw_Data/movies_all_streaming.csv' WITH CSV HEADER;
-- \copy tv_shows_all_streaming FROM '/full/path/to/Raw_Data/tv_shows_all_streaming.csv' WITH CSV HEADER;

-- 4. final table will be created by joins.sql
