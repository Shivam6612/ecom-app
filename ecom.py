import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title("this is a app for ecom i am creating")
    st.sidebar.title("You can upload your file here")
    upload_file=st.sidebar.file_uploader("upload your file",type=['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data=pd.read_csv(upload_file)
            else:
                data=pd.read_excel(upload_file)
            st.sidebar.success("file uplaoded successfully")


            st.subheader("I am going to show you a data details")
            st.dataframe(data.head())

            st.subheader("Let's See Some more Details in this data")
            st.write("Shape of the data",data.shape)
            st.write("The column names inside the data is",data.columns)
            st.write("Missing Values into Column",data.isnull().sum())

            st.subheader("I will show you buit of Stats")
            st.write(data.describe())
            
            

        except Exception as e:
            print(e)

if __name__=="__main__":
    main()