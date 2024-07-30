import streamlit as st
import pandas as pd
import csv
import pickle as pk


#title
st.title('Salary Prediction')

#Open the file in binary mode and loading the pickled file
with open('model.pickle','rb') as file:
    model= pk.load(file)

#form
age = st.number_input("Enter age :", 20, 65)
exp = st.number_input("Enter years of Experience:", 0, 30)
education = st.selectbox("Select Education: ", ["Bachelor's","Master's","PhD"])
if st.button("Submit"):
    if education == "Bachelor's":
        b = 1; m = 0; p = 0
    elif education == "Master's":
        b = 0; m = 1; p = 0
    else:
        b = 0; m = 0; p =1

    df = pd.DataFrame({
        'Age':[age],
        'Years of Experience':[exp],
        "Bachelor's":[b],
        "Master's":[m],
        "PhD":[p]
    })
    df
    
    result = model.predict(df)
    st.write("Your salary would be :" ,result)
         
    