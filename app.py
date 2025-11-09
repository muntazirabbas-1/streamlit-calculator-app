import streamlit as st

st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("A basic calculator built with Streamlit")

# User inputs
num1 = st.number_input("Enter first number:", format="%.10f")
operation = st.selectbox("Select operation:", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"])
num2 = st.number_input("Enter second number:", format="%.10f")

# Perform calculation
result = None
if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (×)":
            result = num1 * num2
        elif operation == "Divide (÷)":
            if num2 == 0:
                st.error("Division by zero is not allowed!")
            else:
                result = num1 / num2
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display result
if result is not None:
    st.success(f"Result: **{result}**")
