import streamlit as st # import streamlit
import pandas as pd # import pandas
import plotly.express as px # import plotly

st.title("CSV Data Analyzer")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    with col4:
        st.metric("Duplicate Rows", df.duplicated().sum())

    st.subheader("Data Quality Report")

    st.write("Missing Values Per Column")

    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ["Column", "Missing Values"]

    st.dataframe(missing_values)

    st.write("Data Types")

    dtypes = df.dtypes.reset_index()
    dtypes.columns = ["Column", "Data Type"]

    st.dataframe(dtypes)

    st.write("Dataset Info")
    st.write(df.head())

    st.subheader("Statistical Summary")

    st.dataframe(df.describe())


    st.subheader("Data Visualization") 

    numeric_cols = df.select_dtypes(include="number").columns # select numeric columns

    # Create column selector
    selected_col = st.selectbox(
        "Select a numeric column",
        numeric_cols
    ) 

    # Create Histogram
    fig = px.histogram(
        df,
        x=selected_col,
        title=f"Distribution of {selected_col}"
    )

    st.plotly_chart(fig)


    # Correlation Heatmap
    if len(numeric_cols) > 1:

        st.subheader("Correlation Heatmap")

        corr = df.corr(numeric_only=True)
        st.dataframe(corr)

    else:
        st.info(
            "Correlation analysis requires at least 2 numeric columns."
        )


    # Scatter Plot
    st.subheader("Scatter Plot Analysis")

    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)

        with col1:
            x_axis = st.selectbox(
                "Select X Axis",
                numeric_cols,
                key="x_axis"
            )

        with col2:
            y_axis = st.selectbox(
                "Select Y Axis",
                numeric_cols,
                key="y_axis"
            )

        scatter_fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            title=f"{y_axis} vs {x_axis}"
        )

        st.plotly_chart(scatter_fig)

    else:
        st.info("Scatter plot requires at least 2 numeric columns.")


    # Box Plot (Outlier Detection)
    st.subheader("Outlier Detection")

    box_col = st.selectbox(
        "Select Column for Outlier Analysis",
        numeric_cols,
        key="boxplot"
    )

    box_fig = px.box(
        df,
        y=box_col,
        title=f"Outlier Analysis - {box_col}"
    )

    st.plotly_chart(box_fig)


    # Dataset Filtering
    st.subheader("Filter Datasets")

    rows_to_show = st.slider(
        "Number of rows to display",
        5, # min
        100, # max
        10 # default
    )

    st.dataframe(df.head(rows_to_show))


    # Download Cleaned Dataset
    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="analyzed_dataset.csv",
        mime="text/csv"
    )