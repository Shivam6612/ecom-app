import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import logging
from typing import Union

# Configure logging
logging.basicConfig(level=logging.INFO)

def load_data(upload_file) -> Union[pd.DataFrame, None]:
    """Loads CSV or Excel file and returns DataFrame"""
    try:
        if upload_file.name.endswith('.csv'):
            return pd.read_csv(upload_file)
        else:
            return pd.read_excel(upload_file)
    except Exception as e:
        logging.error(f"Failed to load file: {e}")
        return None

def show_data_overview(df: pd.DataFrame) -> None:
    """Displays basic details and overview of the DataFrame"""
    with st.expander("🔍 Data Preview"):
        st.dataframe(df.head())

    with st.expander("📊 Data Summary"):
        st.write("**Shape of the data:**", df.shape)
        st.write("**Column Names:**", df.columns.tolist())
        st.write("**Missing Values:**", df.isnull().sum())

    if st.checkbox("Show descriptive statistics"):
        st.write(df.describe())

def show_visuals(df: pd.DataFrame) -> None:
    """Displays simple Seaborn plots"""
    st.subheader("📈 Data Visualizations")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    if not numeric_cols:
        st.info("No numeric columns available for visualization.")
        return

    selected_col = st.selectbox("Select a column for distribution plot", numeric_cols)
    fig, ax = plt.subplots()
    sns.histplot(df[selected_col], kde=True, ax=ax)
    st.pyplot(fig)

def main():
    st.set_page_config(page_title="E-commerce Data Analyzer", layout="wide")
    st.title("🛒 E-commerce Data Analyzer App")
    st.markdown("Upload your dataset to explore it interactively.")

    st.sidebar.header("📂 Upload your file")
    upload_file = st.sidebar.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

    if upload_file is not None:
        df = load_data(upload_file)
        if df is not None:
            st.sidebar.success("✅ File uploaded successfully")
            show_data_overview(df)
            show_visuals(df)
        else:
            st.sidebar.error("❌ Error loading the file. Check format and try again.")
    else:
        st.sidebar.info("Please upload a CSV or Excel file to get started.")

if __name__ == "__main__":
    main()
