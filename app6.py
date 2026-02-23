import streamlit as st

st.title("Simple Registration Form")

# Create Form
with st.form("my_form"):
    
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", step=1)
    city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Nashik", "Pune"])
    gender = st.radio("Select your gender", ["Male", "Female", "Other"])
    
    submit = st.form_submit_button("Submit")

# After Submit
if submit:
    st.success("Form Submitted Successfully ")
    st.write(" Your Details:")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("City:", city)
    st.write("Gender:", gender)