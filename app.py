import streamlit as st
import pickle

reg=pickle.load(open("house_pred.pkl", "rb"))

st.title("House Price Prediction APP")

area=st.number_input("Input Area (in sqft)",min_value=100)

import streamlit as st

bed = st.selectbox("Select bedrooms", options=[1,2,3,4,5,6])



location_score=st.number_input("Input Location Score",min_value=1.0)

bath_room=st.slider("Input Bath Rooms",1,4)

age=st.slider("Input Age of the House",0,50)

if st.button("Predict Price"):
    input_data=[[area, bed, location_score, bath_room, age]]
    prediction=reg.predict(input_data)
    st.success(f"Estimated Price for this House is: ${prediction[0]}")
