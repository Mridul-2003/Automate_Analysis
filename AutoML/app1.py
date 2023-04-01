# Importing libraries.
import streamlit as st

from activities.activity import init_sidebar_content, eda, vis, ml
from ml.mlmodel import MLDataset

# Main method.
def main():
    '''
    Description: 
            Main method where all the functionalities of the app resides.
            
    Parameters: 
            None
    
    Returns: 
            Nothing
    '''
    
    
   
   
        activity_mode = st.sidebar.selectbox("Choose an activity", ["Exploratory Data Analysis", "Visualization", "Machine Learning Models"])
        st.write('\n\n')
        
        # Dataset selection.
        dataset_name = st.selectbox("Pick a dataset", ["Iris", "Breast Cancer", "Wine Quality", "Mnist Digits", "Boston Houses", 'Diabetes'])
        dataset = MLDataset(dataset_name)
        df = dataset.get_dataframe()  

        if activity_mode == 'Exploratory Data Analysis':
            eda(df)
        if activity_mode == 'Visualization':
            vis(df)
        if activity_mode == 'Machine Learning Models':
            ml(df)
            
    
            
# Application starts executing here.                
if __name__ == "__main__":
    main()