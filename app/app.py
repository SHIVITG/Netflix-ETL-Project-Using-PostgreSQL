"""Streamlit dashboard for Netflix data."""
import streamlit as st
import plotly.express as px
import pandas as pd
from sqlalchemy import text
from scripts.db_connection import get_engine

# initialize engine
engine = get_engine()

@st.cache_data

def load_data():
    query = "SELECT * FROM netflix_final"
    return pd.read_sql(query, engine)


def main():
    st.title("Netflix Content Analytics Dashboard")

    df = load_data()

    st.sidebar.header("Filters")
    type_filter = st.sidebar.multiselect("Type", options=df['type'].unique(), default=df['type'].unique())
    year_range = st.sidebar.slider("Release year", int(df['release_year'].min()), int(df['release_year'].max()), (int(df['release_year'].min()), int(df['release_year'].max())))

    filtered = df[(df['type'].isin(type_filter)) &
                  (df['release_year'] >= year_range[0]) &
                  (df['release_year'] <= year_range[1])]

    # histogram of release years
    fig1 = px.histogram(filtered, x="release_year", title="Titles by Release Year")
    st.plotly_chart(fig1)

    # count by country
    top_countries = (filtered.groupby('country').size().reset_index(name='count')
                     .sort_values('count', ascending=False).head(10))
    fig2 = px.bar(top_countries, x='country', y='count', title='Top 10 Countries')
    st.plotly_chart(fig2)

    st.write("## Sample of dataset")
    st.dataframe(filtered.head())


if __name__ == '__main__':
    main()
