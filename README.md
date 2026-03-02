# Netflix ETL Project
This ETL project combines multiple Netflix data sources from Kaggle into postgreSQL table &amp; mapping SQL queries to UI in Python Flask.


## Data Sources

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
- Dropping rows from the merged data with null values


## Load

Two dataframes were created in PostgreSQL which merge the data from Source 3 to Sources 1 and 2 (as separate dataframes).  Since the final fields in each of these dataframes are the same, they can be appended to the same table in postgreSQL.  A schema file to set up a database called 'AreYouStillWatching_db' and the 'final' table for these merged dataframes is included ([AreYouStillWatching_schema.sql](AreYouStillWatching_schema.sql))

In the jupyter notebook, the sqlalchemy module was used to connect to the database and append the dataframes to the 'final' table.  After the dataframes are appended to the table, the table is loaded back into the jupyter notebook using pandas 'read_sql' method and a copy of the table is saved as a CSV file using 'to_sql'.  The CSV copy of the 'final' table is saved in the Output folder. __Please note: You will need to have the psycopg2 module installed to use the sqlalchemy module with postgreSQL.__

The jupyter notebook also generates an audit report to see how long each step of the ETL process took to complete, and how many movie and tv show titles were dropped in the final merged dataframes due to filtering for Netflix titles and null values.  The time module is used to track the current time at the beginning and end of the extract, transform, and load phases of the process.