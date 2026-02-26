import streamlit as st
import pandas as pd
import pickle

data=pd.read_excel(r"C:\Users\bhanu\OneDrive\Desktop\for llm\student_pass_fail_dataset.xlsx")
st.write("hello tanvi")

with open('lr.pkl','rb') as f:
    model=pickle.load(f) 

st.title('Student Pass/Fail Prediction')
st.info('Checking Based on Study Hours,Attendance and Previous Score')    

with st.form('prediction'):
    study_hour=st.number_input('SHours',min_value=0,max_value=10)
    atten=st.number_input('Attendance',min_value=35,max_value=100,step=10)
    prevscore=st.number_input('PreviousScore',min_value=0,max_value=100,step=10)
    submit_button=st.form_submit_button('Start Prediction')

    if submit_button:
        new_data=[[study_hour,atten,prevscore]]
        result=model.predict(new_data)

        if result[0]==1:
            st.success('Student Will Pass')
            st.snow()
        else:
            st.error('Student Will Fail')    
            st.toast('you failed')