import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main(): #Title and Sidebar
    st.title("Aura Data Visualization")
    st.sidebar.title("Files Section")
    upload_file = st.sidebar.file_uploader("Upload Your File here", type=['csv', 'xlsx'])

    try:  # allowing my tool to access any type of file
        file_name = upload_file.name.lower()
        if file_name.endswith(".csv"):
            data = pd.read_csv(upload_file)
        elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            data = pd.read_excel(upload_file)
        elif file_name.endswith(".json"):
            data = pd.read_json(upload_file)
        elif file_name.endswith(".xml"):
            data = pd.read_xml(upload_file)
        else:
            st.error("Unsupported file format")
            st.stop()

        st.sidebar.success("File uploaded successfully")
        st.subheader("Visualized data")
        st.dataframe(data.head())
        st.subheader("Lets see some more details in data")
        st.write("Shape of the the data as Row,Column:",data.shape)
        st.write("The column name inside data is ",data.columns)
        st.write("Missing value into column",data.isnull().sum())

        st.subheader("Lets see some more details in data")
        st.write(data.describe())

    except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
