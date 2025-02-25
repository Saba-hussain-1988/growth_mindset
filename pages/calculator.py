import streamlit as st

# Title of the app
st.title("🧮 Simple Calculator")

# Input field for number 1
num1 = st.number_input("Enter first number", step=1.0)
# num2 = st.number_input("Enter second number", step=1.0)

# Select operation
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division", "Module", "Square", "Cube", "Power"])

# Input field for number 2
num2 = st.number_input("Enter second number", step=1.0)

# Perform calculation when button is clicked
if st.button("Calculate"):
    if operation == "Square" or operation == "Cube":
        if operation == "Square":
            result = num1 * num1
            st.success(f"Result: {num1}** = {result}")

        if operation == "Cube":
            result = num1 ** 3
            st.success(f"Result: {num1}**3 = {result}")

    else :
        if operation == "Addition":
            result = num1 + num2
            st.success(f"Result: {num1} + {num2} = {result}")
    
        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"Result: {num1} - {num2} = {result}")
    
        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"Result: {num1} × {num2} = {result}")
    
        elif operation == "Division" or operation == "Module":
            if num2 == 0:
                st.error("❌ Division by zero is not allowed!")
            else:
                if operation == "Division":
                    result = num1 / num2
                    st.success(f"Result: {num1} ÷ {num2} = {result}")

                if operation == "Module":
                    result = num1 % num2
                    st.success(f"Result: {num1} % {num2} = {result}")


