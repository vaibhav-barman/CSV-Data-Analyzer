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
├── example_screenshots/
│   ├── correlation_heatmap.png
│   ├── data_visualization.png
│   ├── dataset_overview.png
│   ├── download_dataset_button.png
│   ├── filtering_dataset.png
│   ├── outlier_detection.png
│   ├── scatter_plot_analysis.png
│   └── statistical_summary.png
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/vaibhav-barman/CSV-Data-Analyzer
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

### Dataset Overview

![Dataset Overview](example_screenshots/dataset_overview.png)

### Statistical Summary

![Statistical Summary](example_screenshots/statistical_summary.png)

### Data Visualization

![Data Visualization](example_screenshots/data_visualization.png)

### Correlation Analysis

![Correlation Analysis](example_screenshots/correlation_heatmap.png)

### Scatter Plot Analysis

![Scatter Plot Analysis](example_screenshots/scatter_plot_analysis.png)

### Outlier Detection

![Outlier Detection](example_screenshots/outlier_detection.png)

### Dataset Filtering

![Dataset Filtering](example_screenshots/filtering_dataset.png)

### Dataset Export

![Dataset Export](example_screenshots/download_dataset_button.png)


## Future Improvements

* Correlation heatmap visualization
* Data cleaning operations
* Sidebar navigation
* PDF report generation
* Machine learning integration

## Author

Vaibhav Barman
