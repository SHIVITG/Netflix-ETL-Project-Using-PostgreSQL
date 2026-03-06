import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64

# Set page config with custom theme
st.set_page_config(
    page_title="Netflix Analytics Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for fancy styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .sidebar-content {
        background: linear-gradient(180deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
    }
    .chart-container {
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv('../data/processed_data/netflix_final.csv')
    # Add some derived columns
    df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float)
    df['release_decade'] = (df['release_year'] // 10) * 10
    return df

df = load_data()

# Animated title
st.markdown('<h1 class="main-header">🎬 Netflix Analytics Pro</h1>', unsafe_allow_html=True)

# Sidebar with fancy styling
st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
st.sidebar.header("🎛️ Interactive Filters")

# Content type filter with icons
content_types = df['type'].unique()
type_icons = {'Movie': '🎥', 'TV Show': '📺'}
selected_types = st.sidebar.multiselect(
    "Select Content Types",
    content_types,
    default=content_types,
    format_func=lambda x: f"{type_icons.get(x, '📺')} {x}"
)

# Year range filter
min_year, max_year = int(df['release_year'].min()), int(df['release_year'].max())
year_range = st.sidebar.slider(
    "Release Year Range",
    min_year, max_year, (min_year, max_year)
)

# Country filter
if 'country' in df.columns:
    countries = sorted(df['country'].dropna().unique())
    selected_countries = st.sidebar.multiselect(
        "Select Countries (leave empty for all)",
        countries,
        default=[]
    )

# Rating filter
if 'rating' in df.columns:
    ratings = sorted(df['rating'].dropna().unique())
    selected_ratings = st.sidebar.multiselect(
        "Select Ratings",
        ratings,
        default=[]
    )

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Filter data
filtered_df = df[df['type'].isin(selected_types)]
filtered_df = filtered_df[
    (filtered_df['release_year'] >= year_range[0]) &
    (filtered_df['release_year'] <= year_range[1])
]

if selected_countries:
    filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]

if selected_ratings:
    filtered_df = filtered_df[filtered_df['rating'].isin(selected_ratings)]

# Fancy metrics with animations
st.markdown('<div class="chart-container">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{len(filtered_df):,}</h2>
        <p>Total Content</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    movies = len(filtered_df[filtered_df['type'] == 'Movie'])
    st.markdown(f"""
    <div class="metric-card">
        <h2>{movies:,}</h2>
        <p>🎥 Movies</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    tv_shows = len(filtered_df[filtered_df['type'] == 'TV Show'])
    st.markdown(f"""
    <div class="metric-card">
        <h2>{tv_shows:,}</h2>
        <p>📺 TV Shows</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_year = int(filtered_df['release_year'].mean())
    st.markdown(f"""
    <div class="metric-card">
        <h2>{avg_year}</h2>
        <p>📅 Avg Release Year</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Interactive charts in tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribution", "🌍 Geography", "📈 Trends", "🎯 Insights"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Enhanced pie chart
        type_counts = filtered_df['type'].value_counts()
        fig1 = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title="Content Type Distribution",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.4
        )
        fig1.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Rating distribution
        if 'rating' in filtered_df.columns:
            rating_counts = filtered_df['rating'].value_counts().head(10)
            fig2 = px.bar(
                x=rating_counts.index,
                y=rating_counts.values,
                title="Top Ratings Distribution",
                color=rating_counts.values,
                color_continuous_scale='RdYlBu_r'
            )
            st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    # World map of content (if country data allows)
    if 'country' in filtered_df.columns:
        country_counts = filtered_df['country'].value_counts().head(20)
        fig3 = px.choropleth(
            locations=country_counts.index,
            locationmode="country names",
            color=country_counts.values,
            title="Content by Country",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Release year trend
        year_counts = filtered_df['release_year'].value_counts().sort_index()
        fig4 = px.area(
            x=year_counts.index,
            y=year_counts.values,
            title="Content Release Trend",
            color_discrete_sequence=['#FF6B6B']
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        # Decade distribution
        decade_counts = filtered_df['release_decade'].value_counts().sort_index()
        fig5 = px.bar(
            x=decade_counts.index.astype(str) + 's',
            y=decade_counts.values,
            title="Content by Decade",
            color=decade_counts.values,
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.header("🎯 Key Insights")

    # Generate insights
    insights = []

    # Content type ratio
    if len(filtered_df) > 0:
        movie_ratio = len(filtered_df[filtered_df['type'] == 'Movie']) / len(filtered_df)
        insights.append(f"📊 **{movie_ratio:.1%}** of content are Movies")

    # Most productive year
    if len(year_counts) > 0:
        top_year = year_counts.idxmax()
        insights.append(f"📈 **{top_year}** was the most productive year with {year_counts.max()} releases")

    # Top country
    if 'country' in filtered_df.columns and len(country_counts) > 0:
        top_country = country_counts.index[0]
        insights.append(f"🌍 **{top_country}** produces the most content")

    # Average duration
    if 'duration_minutes' in filtered_df.columns:
        avg_duration = filtered_df['duration_minutes'].mean()
        if not pd.isna(avg_duration):
            insights.append(f"⏱️ Average content duration: **{avg_duration:.0f} minutes**")

    for insight in insights:
        st.markdown(f"- {insight}")

    st.markdown('</div>', unsafe_allow_html=True)

# Data exploration section
st.header("🔍 Data Explorer")
col1, col2 = st.columns([3, 1])

with col1:
    st.dataframe(filtered_df.head(20), use_container_width=True)

with col2:
    st.download_button(
        label="📥 Download Filtered Data",
        data=filtered_df.to_csv(index=False),
        file_name='netflix_filtered_pro.csv',
        mime='text/csv',
        use_container_width=True
    )

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit & Plotly | Netflix Data Analytics Pro")