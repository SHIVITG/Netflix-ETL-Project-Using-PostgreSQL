# Netflix Data Engineering & Analytics Project

This project demonstrates a **complete end-to-end data pipeline** using Netflix datasets. Students start with raw CSV files, integrate them using **PostgreSQL JOIN operations**, analyze the data using **SQL**, and finally build a **Python-based interactive dashboard UI**.

The project simulates a real-world workflow used by **data engineers, analysts, and data scientists**.

---

# Project Architecture

```
![Netflix ETL Pipeline Architecture](ProjectWorkflow.png)
```

Students will learn:

* Data Engineering fundamentals
* PostgreSQL database management
* SQL JOIN operations
* Data analytics using SQL
* Python database connectivity
* Interactive dashboard development

---

# Data Sources

The project uses three datasets from Kaggle.

| Dataset                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| netflix_titles.csv         | Metadata about Netflix movies and TV shows    |
| movies_all_streaming.csv   | Movies available across streaming platforms   |
| tv_shows_all_streaming.csv | TV shows available across streaming platforms |


Data sources are CSV files available from Kaggle.com, which include data about movies and TV shows on popular streaming services.  The CSV files were downloaded manually from the links shown below, and are saved in the Resources folder of the repository.

|Source No.|Link with Description|Source Last Updated|Download Date|File name in Resources folder|
|---|---|---|---|---|
|1|[List of TV shows on multiple streaming services](https://www.kaggle.com/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney)|2020-05-25|2021-03-06|tv_shows_all_streaming.csv|
|2|[List of Movies on multiple streaming services](https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney)|2020-05-22|2021-03-06|movies_all_streaming.csv|
|3|[List of TV shows and Movies on Netflix](https://www.kaggle.com/shivamb/netflix-shows)|2021-01-18|2021-03-06|netflix_titles.csv|

Sources 1 and 2 include ratings from Rotten Tomatoes and IMDb.  Source 3 includes TV/Movie Ratings (MPAA) and Target Audience Age.

## Transform
Used Excel file ([ETL_Netflix_Major.xlsx](Transformed_Data/ETL_Netflix_Major.xlsx)) to plan the transformations needed to comply with business rules for the final database table.  Transformations include dropping unneeded data columns, changing dates from object/string types to datetime types, and renaming columns to match case for inner join and import into the final postgreSQL table.

Since the netflix_titles.csv file contains ratings (MPAA) and target audience age data for TV shows and movies on Netflix only, and the tv_shows_all_streaming.csv and movies_all_streaming.csv files contain Rotten Tomatoes and IMDb ratings data, we opted to merge these data sources into a single table that would include all of these data.  We also wanted to remove any titles with null values.  The transform includes:
- Finding only Netflix titles for TV shows and movies (Sources 1 and 2)
- Joining TV shows and movies data to Netflix titles data on title name and year of release (Source 3 to Source 1, Source 3 to Source 2)
- Dropping rows from the merged data with null values.

---
---

# Step 1 — Extract (Raw Data)

Download the datasets and place them in a Raw_Data folder.

```
Raw_Data/
    netflix_titles.csv
    movies_all_streaming.csv
    tv_shows_all_streaming.csv
```

These files represent the **raw input data sources**.

---

# Step 2 — Load Raw Data into PostgreSQL

Create the project database.

```
AreYouStillWatching_db
```

Create tables matching the raw datasets.

### Netflix Titles Table

```sql
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
```

### Movies Streaming Table

```sql
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
```

### TV Shows Streaming Table

```sql
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
```

Load CSV files using PostgreSQL `COPY`.

---

# Step 3 — Data Integration using SQL JOIN

Combine the datasets using SQL joins.

### Movies + Netflix Metadata

```sql
SELECT
nt.title,
nt.type,
nt.release_year,
nt.country,
nt.rating,
ma.imdb,
ma.rotten_tomatoes
FROM netflix_titles nt
JOIN movies_all_streaming ma
ON nt.title = ma.title
AND nt.release_year = ma.year
WHERE ma.netflix = 1;
```

### TV Shows + Netflix Metadata

```sql
SELECT
nt.title,
nt.type,
nt.release_year,
nt.country,
nt.rating,
ta.imdb,
ta.rotten_tomatoes
FROM netflix_titles nt
JOIN tv_shows_all_streaming ta
ON nt.title = ta.title
AND nt.release_year = ta.year
WHERE ta.netflix = 1;
```

---

# Step 4 — Create Final Integrated Table

```sql
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
ma.imdb,
ma.rotten_tomatoes
FROM netflix_titles nt
JOIN movies_all_streaming ma
ON nt.title = ma.title
AND nt.release_year = ma.year
WHERE ma.netflix = 1;
```

Append TV show data to the table.

---

# Step 5 — Business Analytics Queries

Students perform SQL analysis.

Examples:

### Movies vs TV Shows

```sql
SELECT type, COUNT(*)
FROM netflix_final
GROUP BY type;
```

### Top 5 countries with most content

```sql
SELECT country, COUNT(*)
FROM netflix_final
GROUP BY country
ORDER BY COUNT(*) DESC
LIMIT 5;
```

### Longest movie

```sql
SELECT title, duration
FROM netflix_final
WHERE type='Movie'
ORDER BY duration DESC
LIMIT 1;
```

### Content classification (violence keywords)

```sql
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
```

---

# Step 6 — Python Database Integration

Connect Python to PostgreSQL.

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
"postgresql://username:password@localhost:5432/AreYouStillWatching_db"
)

df = pd.read_sql("SELECT * FROM netflix_final", engine)
```

---

# Step 7 — Build an Interactive UI Dashboard

Students will build a dashboard using:

* Streamlit
* Plotly

These tools allow students to create **interactive analytics dashboards directly from Python**.

---

# Example Dashboard Code

```python
import streamlit as st
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
"postgresql://username:password@localhost:5432/AreYouStillWatching_db"
)

df = pd.read_sql("SELECT * FROM netflix_final", engine)

st.title("Netflix Content Analytics Dashboard")

fig = px.histogram(df, x="release_year")

st.plotly_chart(fig)
```

---

# Running the Project

The repository follows a consistent lowercase, underscore naming convention. A helper script (`rename_dirs.py`) is included that can rename the directories if you need to apply the conventions automatically.

After placing the CSV files in the `raw_data/` folder (or run the script to rename) you can execute the end-to-end pipeline in two different ways.

1. **SQL-only (psql)**
   * Create the database (if not already created):
     ```sh
     createdb AreYouStillWatching_db
     psql -d AreYouStillWatching_db -f sql/schema.sql
     psql -d AreYouStillWatching_db -c "\copy netflix_titles FROM 'raw_data/netflix_titles.csv' CSV HEADER"
     psql -d AreYouStillWatching_db -c "\copy movies_all_streaming FROM 'raw_data/movies_all_streaming.csv' CSV HEADER"
     psql -d AreYouStillWatching_db -c "\copy tv_shows_all_streaming FROM 'raw_data/tv_shows_all_streaming.csv' CSV HEADER"
     psql -d AreYouStillWatching_db -f sql/joins.sql
     ```
   * Run analytics queries with `psql -f PostgreSQL_data/analytics_queries.sql` or interactively.

2. **Python-driven pipeline**
   * Install dependencies from `requirements.txt` (e.g. `pip install -r requirements.txt`).
   * Set PostgreSQL credentials via environment variables (`PGUSER`, `PGPASSWORD`, `PGDATABASE`, etc.) or modify `scripts/db_connection.py`.
   * Run the helper script:
     ```sh
     python3 scripts/run_pipeline.py
     ```
     This will execute the schema script, copy the raw CSVs into the database, and create the `netflix_final` table.

3. **Exploration and dashboard**
   * After the data is loaded you can open `scripts/data_analysis.ipynb` with Jupyter to explore the data or use the sample code above.
   * To launch the Streamlit dashboard run:
     ```sh
     streamlit run app/app.py
     ```

# Example Dashboard Features

Students can create visualizations such as:

* Movies vs TV shows distribution
* Content released per year
* Top genres
* Top countries producing Netflix content
* IMDb rating distribution
* Actor and director frequency

---

# Repository Structure

```

raw_data/
    netflix_titles.csv
    movies_all_streaming.csv
    tv_shows_all_streaming.csv

transformed_data/
    ETL_Netflix_Major.xlsx
    Netflix_ETL_Basic.xlsx

sql/
    schema.sql
    joins.sql
    analytics_queries.sql

scripts/
    db_connection.py
    data_analysis.ipynb
    run_pipeline.py

app/
    app.py

rename_dirs.py  (helper for renaming folders)

README.md
```

---

# Skills Learned

Students will gain practical experience in:

* Data Engineering pipelines
* PostgreSQL database design
* SQL JOIN operations
* Data integration
* SQL analytics
* Python data analysis
* Dashboard development
