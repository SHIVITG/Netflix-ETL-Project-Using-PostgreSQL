-- SQL script to create integrated "netflix_final" table
-- run after loading the raw tables

DROP TABLE IF EXISTS netflix_final;
CREATE TABLE netflix_final AS
SELECT
    nt.title,
    nt.type,
    nt.release_year,
    nt.country,
    nt.rating,
    nt.duration,
    nt.listed_in,
    nt.description,
    COALESCE(ma.imdb, ta.imdb)           AS imdb,
    COALESCE(ma.rotten_tomatoes, ta.rotten_tomatoes) AS rotten_tomatoes
FROM netflix_titles nt
LEFT JOIN movies_all_streaming ma
    ON nt.title = ma.title
    AND nt.release_year = ma.year
    AND ma.netflix = 1
LEFT JOIN tv_shows_all_streaming ta
    ON nt.title = ta.title
    AND nt.release_year = ta.year
    AND ta.netflix = 1
WHERE (ma.netflix = 1 OR ta.netflix = 1);

-- add indexes for performance
CREATE INDEX idx_netflix_final_type ON netflix_final(type);
CREATE INDEX idx_netflix_final_year ON netflix_final(release_year);
CREATE INDEX idx_netflix_final_country ON netflix_final(country);

-- optional: verify row count
-- SELECT COUNT(*) FROM netflix_final;
