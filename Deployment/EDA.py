# import library
import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image


def app():
    # Sidebar options
    st.title('Model Deployment')
    st.sidebar.header('Exploratory Data Analysis')
    eda_option = st.sidebar.selectbox('Select Analysis', ['Melanoma Cancer Distribution', 'Display Images Melanoma Cancer'])

    # Title
    st.markdown("<h2 style='text-align: center;'>Exploratory Data Analysis for Melanoma Cancer</h2>", unsafe_allow_html=True)
    

    if eda_option == 'Melanoma Cancer Distribution':

    # Menampilkan grafik dengan st.image
        st.markdown("<h3 style='text-align: center;'>Melanoma Cancer Distribution</h3>", unsafe_allow_html=True)
        st.image('Distribution Dataset.png', caption='Data Distribution for Train and Test Data')
        interpretation = """
        Based on the Train and Test Data Distribution Visualization:

            - The Train Data contains 5,590 instances of the Malignant class and 6,289 instances of the Benign class.

            - The Test Data contains 1,000 instances of the Malignant class and 1,000 instances of the Benign class.
        """
        st.write(interpretation)
        
    if eda_option == 'Display Images Melanoma Cancer':

        # Menampilkan gambar train dataset dengan st.image
        st.markdown("<h3 style='text-align: center;'>Melanoma Cancer Benign and Malignant</h3>", unsafe_allow_html=True)
        st.image('train dataset.png', caption='Melanoma Skin Cancer Images in Training Data')
        interpretation = """
        The image shows Benign and Malignant types of Melanoma Cancer in the Training dataset.
        """
        st.write(interpretation)

        # Menampilkan gambar test dataset dengan st.image
        st.image('test dataset.png', caption='Melanoma Skin Cancer Images in Testing Data')
        interpretation = """
        The image shows Benign and Malignant types of Melanoma Cancer in the Testing dataset.
        """
        st.write(interpretation)

# Run the Streamlit app
if __name__ == '__main__':
    app()

