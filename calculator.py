import streamlit as st

st.title("Simple Calculator")
st.write("This is a basic Streamlit app.")

# Simple Calculator
number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")
operation = st.selectbox("Choose the operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = number1 + number2
    elif operation == "Subtract":
        result = number1 - number2
    elif operation == "Multiply":
        result = number1 * number2
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Cannot divide by zero"
    st.write(f"The result is: {result}")
