"""Script to execute the ETL pipeline: create tables, load data, perform joins."""
import os
import subprocess
import sys
from sqlalchemy import text
from db_connection import get_engine


def run_sql_file(engine, filepath):
    with open(filepath) as f:
        sql = f.read()
    with engine.connect() as conn:
        conn.execute(text(sql))
        conn.commit()


def copy_csv(engine, table_name, csv_path):
    # use psql COPY via sqlalchemy raw connection
    sql = f"COPY {table_name} FROM STDIN WITH CSV HEADER"
    with engine.raw_connection() as conn:
        cur = conn.cursor()
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert(sql, f)
        conn.commit()


def main():
    engine = get_engine()

    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
    schema_path = os.path.join(base, 'schema.sql')
    joins_path = os.path.join(base, 'joins.sql')

    print("Creating schema...")
    run_sql_file(engine, schema_path)

    raw = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'raw_data'))
    files = {
        'netflix_titles': 'netflix_titles.csv',
        'movies_all_streaming': 'movies_all_streaming.csv',
        'tv_shows_all_streaming': 'tv_shows_all_streaming.csv'
    }
    for table, fname in files.items():
        path = os.path.join(raw, fname)
        print(f"Loading {path} into {table}")
        copy_csv(engine, table, path)

    print("Running joins to build final table")
    run_sql_file(engine, joins_path)

    print("Pipeline complete. netflix_final table is ready.")


if __name__ == '__main__':
    main()
