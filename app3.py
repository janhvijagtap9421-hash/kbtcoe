import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter your first number", step=1, format="%d")
num2 = st.number_input("Enter your second number", step=1, format="%d")

operation = st.selectbox("Choose operation", ["add", "sub", "mul", "div"])

if st.button("Calculate"):
    if operation == "add":
        st.write(int(num1 + num2))

    elif operation == "sub":
        st.write(int(num1 - num2))

    elif operation == "mul":
        st.write(int(num1 * num2))

    elif operation == "div":
        if num2 != 0:
            st.write(int(num1 / num2))  # converts result to integer
        else:
            st.write("Error: Division by zero")