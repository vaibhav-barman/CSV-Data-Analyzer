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