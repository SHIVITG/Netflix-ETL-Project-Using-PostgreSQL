import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# Set page config
st.set_page_config(page_title="Netflix Data Dashboard", page_icon="🎬", layout="wide")

# Set seaborn style for any matplotlib plots
sns.set_style("darkgrid")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('../data/processed_data/netflix_final.csv')
    return df

df = load_data()

# Title
#st.title("🎬 Netflix Data Analysis Dashboard")

col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("images/logo.jpg", width=150)
with col_title:
    st.title("Netflix Data Analysis Dashboard")

# Sidebar
st.sidebar.header("Filters")

# Content type filter
content_types = df['type'].unique()
selected_types = st.sidebar.multiselect("Select Content Types", content_types, default=content_types)

# Filter data
filtered_df = df[df['type'].isin(selected_types)]

# Key metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Content", len(filtered_df))
with col2:
    movies = len(filtered_df[filtered_df['type'] == 'Movie'])
    st.metric("Movies", movies)
with col3:
    tv_shows = len(filtered_df[filtered_df['type'] == 'TV Show'])
    st.metric("TV Shows", tv_shows)

# # Content Type Distribution
# st.header("Content Type Distribution")
# type_counts = filtered_df['type'].value_counts()
# fig1 = px.pie(values=type_counts.values, names=type_counts.index, 
#               title="Distribution of Content Types",
#               color_discrete_sequence=px.colors.qualitative.Set3)
# st.plotly_chart(fig1, use_container_width=True)

# # Release Year Distribution
# st.header("Release Year Distribution")
# if 'release_year' in filtered_df.columns:
#     year_counts = filtered_df['release_year'].value_counts().sort_index()
#     fig2 = px.bar(x=year_counts.index, y=year_counts.values,
#                   title="Content Release by Year",
#                   labels={'x': 'Release Year', 'y': 'Count'},
#                   color=year_counts.values,
#                   color_continuous_scale='Viridis')
#     fig2.update_layout(xaxis_tickangle=-45)
#     st.plotly_chart(fig2, use_container_width=True)

# # Top Countries
# st.header("Top 10 Countries by Content")
# if 'country' in filtered_df.columns:
#     top_countries = filtered_df['country'].value_counts().head(10)
#     fig3 = px.bar(y=top_countries.index, x=top_countries.values, orientation='h',
#                   title="Top 10 Countries by Content Count",
#                   labels={'y': 'Country', 'x': 'Count'},
#                   color=top_countries.values,
#                   color_continuous_scale='Blues')
#     st.plotly_chart(fig3, use_container_width=True)

# # Content Addition Trend
# st.header("Content Addition Trend Over Time")
# if 'date_added' in filtered_df.columns:
#     # Convert to datetime and extract year
#     filtered_df_copy = filtered_df.copy()
#     filtered_df_copy['year_added'] = pd.to_datetime(filtered_df_copy['date_added'], errors='coerce').dt.year
#     yearly_additions = filtered_df_copy['year_added'].value_counts().sort_index()
#     fig4 = px.line(x=yearly_additions.index, y=yearly_additions.values,
#                    title="Content Added by Year",
#                    labels={'x': 'Year Added', 'y': 'Count'},
#                    markers=True)
#     fig4.update_traces(line_color='#FF6B6B', marker_color='#4ECDC4')
#     st.plotly_chart(fig4, use_container_width=True)

# Data Table
st.header("Sample Data")
st.dataframe(filtered_df.head(10))

# Raw data download
st.download_button(
    label="Download filtered data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name='netflix_filtered.csv',
    mime='text/csv'
)