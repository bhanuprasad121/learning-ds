import streamlit as st
import pickle

with open('lr.pkl','rb') as f:
    model=pickle.load(f)

st.title('House Prediction')
st.info('with Sqrft,Bedroom,Age,location')
with st.form('Prediction from'):
    squrfeet=st.number_input('sqr_feet',min_value=500,max_value=4000,step=500)
    nobeds=st.number_input('BedRoom',min_value=1,max_value=5,step=1)
    buildage=st.number_input('Age',min_value=1,max_value=20,step=1)
    loaction=st.number_input('Location',min_value=1,max_value=20,step=1)
    button=st.form_submit_button('Predict House')

    if button:
        PredictHouse=model.predict([[squrfeet,nobeds,buildage,loaction]])[0]
        predicted_value = PredictHouse      
        st.success(f'House Predicted Value: {PredictHouse:.2f}')
        st.balloons()