import streamlit as st
import streamlit.components.v1 as components


import pandas as pd


from sklearn.datasets import load_diabetes
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu



def main():
     #Sidebar
    from PIL import Image
    image_loan=Image.open("ml4.jpg")
    rad = st.sidebar.radio("Navigation",["Home","Analysis","Visualize"])
    # if rad=="Home":
    #     HtmlFile = open("style.css", 'r', encoding='utf-8')
    #     source_code = HtmlFile.read() 
    #     components.html(source_code,width=900, height=700)
    #     # print(source_code)

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</stle>',unsafe_allow_html=True)
        html_temp = """
        <div style="background-color:red;padding:10px">
        <h2 style="color:white;text-align:center;">Automatic Machine Learning </h2>
        <img src=""
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
    if rad == "Analysis":
         
        file_upload=st.sidebar.file_uploader(" ",type=["csv"])
        st.sidebar.image(image_loan,use_column_width=True) 
        html_temp = """
        <div style="background-color:red;padding:10px">
        <h2 style="color:white;text-align:center;">Automatic Machine Learning </h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        st.sidebar.title("Upload Input csv file : ")
        st.subheader('1.Datasets')
        st.write("""
    # Automated Machine Learning
    """)


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
                data = df1.to_csv("new.csv")
                st.write(df1)
                



if __name__ == '__main__':
    main()
