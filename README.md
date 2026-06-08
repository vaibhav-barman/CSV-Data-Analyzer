# CSV Data Analyzer

A Streamlit-based web application for performing Exploratory Data Analysis (EDA) on CSV datasets.

## 🚀 Live Demo

https://csv-data-analyzer-by-vaibhav-barman.streamlit.app/

## Features

* Upload and analyze CSV files
* Dataset overview metrics

  * Total rows
  * Total columns
  * Missing values count
  * Duplicate rows count
* Data quality analysis

  * Missing values per column
  * Data types inspection
* Statistical summary of numeric columns
* Interactive histogram visualization
* Correlation analysis
* Interactive scatter plot analysis
* Outlier detection using box plots
* Dataset filtering
* Download analyzed dataset

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly

## Project Structure

```text
CSV-Data-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd csv-data-analyzer
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the application

```bash
streamlit run app.py
```

## Screenshots

Add screenshots of:

* Dataset Overview
* Data Quality Report
* Histogram Visualization
* Scatter Plot Analysis
* Outlier Detection

## Future Improvements

* Correlation heatmap visualization
* Data cleaning operations
* Sidebar navigation
* PDF report generation
* Machine learning integration

## Author

Vaibhav Barman
