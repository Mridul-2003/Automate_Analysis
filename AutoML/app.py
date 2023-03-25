import streamlit as st
import openai
import pandas as pd
import pandas_profiling
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import load_diabetes
from streamlit_pandas_profiling import st_profile_report
from streamlit_chat import message


st.write("""
# Automated Machine Learning
""")

#Sidebar
html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:white;text-align:center;">Automatic Machine Learning </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
from PIL import Image
image_loan=Image.open("ml4.jpg")
st.sidebar.title("Upload Input csv file : ")
file_upload=st.sidebar.file_uploader(" ",type=["csv"])
st.sidebar.image(image_loan,use_column_width=True) 

st.subheader('1.Datasets')


if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.write(df)
    df1 = df.dropna()
    if st.button('Run Modeling'):
        st.title("Exploratory Data Analysis")
        profile_df = df.profile_report()
        st_profile_report(profile_df)
    if st.button("No. of Missing values"):
            st.write(df.isna().sum())
    if st.button('Drop Missing values'):
        df1 = df.dropna()
        st.write(df1)




    
    
        
    
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Datasets'):
        diabetes = load_diabetes()
        X = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
        Y = pd.Series(diabetes.target,name='response')
        df = pd.concat([X,Y],axis=1)
        st.markdown('The Diabetes dataset is used as the example.')
        st.write(df.head())
        st.markdown("Shape of Diabetes dataset")
        st.write(df.shape)
        st.title("Exploratory Data Analysis")
        profile_df = df.profile_report()
        st_profile_report(profile_df)
        st.title("Sum of Null Values")
        st.write(df.isna().sum())
        st.title("Dropping Null Values")
        df1 = df.dropna()
        st.write(df1)
