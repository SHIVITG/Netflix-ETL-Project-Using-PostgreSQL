# Netflix Data Dashboard

A Streamlit web application for visualizing and analyzing Netflix content data with interactive Plotly charts.

## Features

- Interactive dashboard with content type filtering
- Key metrics display (total content, movies, TV shows)
- **Interactive pie chart** for content type distribution
- **Colorful bar chart** for release year distribution with gradient colors
- **Horizontal bar chart** for top countries with blue gradient
- **Line chart** showing content addition trends over time
- Sample data preview with filtering
- Data export functionality

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/netflix_etl_project
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Streamlit (if not included in requirements.txt):**
   ```bash
   pip install streamlit
   ```

4. **Ensure data file exists:**
   - The app expects `../data/processed_data/netflix_final.csv` relative to the dashboard folder
   - Make sure this file exists and contains the Netflix dataset

## Running the Applications

### Basic Dashboard (app.py)
```bash
cd dashboard
python3 -m streamlit run app.py
```

### Pro Dashboard (app2.py) - Enhanced Interactive Version
```bash
cd dashboard
python3 -m streamlit run app2.py
```

The Pro version includes:
- Custom gradient themes and animations
- Advanced filtering options (year range, countries, ratings)
- Interactive tabs with multiple chart types
- World map visualization
- Trend analysis with area charts
- AI-generated insights
- Fancy styled components with CSS
   - Streamlit will automatically open your default browser
   - If not, navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## Usage

- Use the sidebar filters to select specific content types
- View metrics and charts that update based on your filters
- Scroll through different visualizations
- Download filtered data as CSV using the download button

## Troubleshooting

- **File not found error:** Ensure the `netflix_final.csv` file exists in the correct path
- **Import errors:** Make sure all required packages are installed
- **Port already in use:** Streamlit runs on port 8501 by default; close other apps using this port or specify a different port with `streamlit run app.py --server.port 8502`

## Data Requirements

The application expects a CSV file with at least these columns:
- `type` (Movie/TV Show)
- `release_year` (numeric)
- `country` (string)

Additional columns will be displayed in the data table but are not required for the core visualizations.