# Netflix ETL & Analytics Project

A comprehensive data engineering and analytics project that demonstrates end-to-end ETL pipeline, database operations, Python analysis, and interactive dashboards using Netflix streaming data.

## Project Overview

This project showcases a complete data pipeline from raw data ingestion to interactive visualization:

- **ETL Pipeline**: Extract, transform, and load Netflix datasets
- **Database Operations**: PostgreSQL table creation, data cleaning, and JOIN operations
- **Data Analysis**: SQL analytics and Python-based exploratory data analysis
- **Interactive Dashboards**: Streamlit applications with advanced visualizations
- **Educational Components**: Student assignment notebooks with TODO tasks

## Project Structure

```
netflix_etl_project/
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── data/
│   ├── processed_data/
│   │   └── netflix_final.csv        # Final processed dataset
│   ├── raw_data/
│   │   ├── netflix_titles.csv       # Netflix titles metadata
│   │   ├── movies_all_streaming.csv # Movies across platforms
│   │   └── tv_shows_all_streaming.csv # TV shows across platforms
│   └── elt_plan/                    # ETL planning documents
├── postgresql_operations/
│   ├── analysis.sql                 # SQL analysis queries
│   ├── joining_tables.sql           # Table join operations
│   └── tables_create_and_clean/
│       ├── cleanup.sql              # Data cleaning scripts
│       ├── movies_all_streaming.sql # Movies table schema
│       ├── netflix_titles.sql       # Netflix titles schema
│       └── tv_shows_all_streaming.sql # TV shows schema
├── python_engine/
│   ├── analysis/                    # Analysis scripts
│   ├── db_connection/
│   │   └── db_connection.py         # Database connection utilities
│   └── notebooks/
│       ├── demo.ipynb               # Introduction to notebooks
│       └── netflix_student_todo.ipynb # Student assignment notebook
└── dashboard/
    ├── app.py                       # Basic Streamlit dashboard
    ├── app2.py                      # Advanced interactive dashboard
    └── README.md                    # Dashboard documentation
```

## Quick Start

### Prerequisites
- Python 3.7+
- PostgreSQL database
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd netflix_etl_project
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database:**
   - Create a database named `netflix_db`
   - Update connection credentials in `python_engine/db_connection/db_connection.py`

## Data Pipeline

### 1. Raw Data Sources
The project uses three Netflix-related datasets:
- `netflix_titles.csv`: Netflix catalog with metadata
- `movies_all_streaming.csv`: Movies availability across platforms
- `tv_shows_all_streaming.csv`: TV shows availability across platforms

### 2. ETL Process
- **Extract**: Load raw CSV files
- **Transform**: Clean data, handle missing values, standardize formats
- **Load**: Import into PostgreSQL tables with proper schemas

### 3. Database Operations
- Table creation scripts in `postgresql_operations/tables_create_and_clean/`
- Data cleaning and JOIN operations
- Analytical queries in `postgresql_operations/analysis.sql`

### 4. Python Analysis
- Database connectivity via `python_engine/db_connection/db_connection.py`
- Data exploration and visualization
- Interactive notebooks for analysis

## Dashboards

### Basic Dashboard (`dashboard/app.py`)
Interactive Streamlit app with:
- Content type filtering
- Key metrics display
- Basic charts (pie, bar, line)
- Data export functionality

### Pro Dashboard (`dashboard/app2.py`)
Enhanced version with:
- Custom CSS styling and animations
- Advanced filtering (year range, countries, ratings)
- Interactive tabs and world map
- Trend analysis and AI insights
- Professional UI/UX design

**To run dashboards:**
```bash
cd dashboard
python3 -m streamlit run app.py      # Basic version
python3 -m streamlit run app2.py     # Pro version
```

## Educational Components

### Student Assignment Notebook
`python_engine/notebooks/netflix_student_todo.ipynb` contains:
- TODO tasks for data loading and exploration
- Guided data cleaning exercises
- Statistical analysis assignments
- Visualization challenges
- Step-by-step learning path

### Demo Notebook
`python_engine/notebooks/demo.ipynb` provides:
- Introduction to Jupyter notebooks
- pandas DataFrame basics
- Missing value handling
- DateTime operations
- .apply() method examples

## Technologies Used

- **Data Processing**: Python, pandas, NumPy
- **Database**: PostgreSQL
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Web Framework**: Streamlit
- **Notebooks**: Jupyter
- **Version Control**: Git

## Key Features

- Complete ETL pipeline implementation
- Interactive data visualizations
- Database integration with Python
- Educational TODO assignments
- Multiple dashboard variants
- Responsive web interfaces
- Data export capabilities

## Configuration

### Database Connection
Update credentials in `python_engine/db_connection/db_connection.py`:
```python
user = "your_username"
password = "your_password"
host = "localhost"
port = 5432
dbname = "netflix_db"
```

### Data Paths
- Raw data: `data/raw_data/`
- Processed data: `data/processed_data/`
- Notebooks: `python_engine/notebooks/`
- Dashboards: `dashboard/`

## Usage Examples

### Running SQL Analysis
```sql
-- Connect to PostgreSQL and run queries from
-- postgresql_operations/analysis.sql
```

### Python Data Analysis
```python
from python_engine.db_connection.db_connection import DatabaseConnection

db = DatabaseConnection()
df = db.execute_query("SELECT * FROM netflix_titles LIMIT 10")
print(df.head())
```

### Dashboard Development
```bash
cd dashboard
python3 -m streamlit run app2.py
# Access at http://localhost:8501
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes. Please refer to individual dataset licenses for usage rights.

## Acknowledgments

- Netflix data from Kaggle
- Streaming platform datasets from Kaggle contributors
- Open source libraries: pandas, Streamlit, Plotly

---

**Built for data engineering and analytics education for class COMP 3610 Database Systems | Shivani Tyagi**
