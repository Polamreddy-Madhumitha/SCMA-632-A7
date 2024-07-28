import streamlit as st

# Set title
st.title("BMI Calculator")

# Add a sidebar
st.sidebar.header("Input your details")

# Get user input from sidebar
height = st.sidebar.number_input("Enter your height (in centimeters):", min_value=0.0, format="%f")
weight = st.sidebar.number_input("Enter your weight (in kilograms):", min_value=0.0, format="%f")

# Add a button to calculate BMI
calculate_button = st.sidebar.button("Calculate BMI")

# Calculate BMI when the button is pressed
if calculate_button:
    if height > 0 and weight > 0:
        height_m = height / 100  # convert height to meters
        bmi = weight / (height_m ** 2)
        st.write(f"Your BMI is {bmi:.2f}")

        # Interpret BMI
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter positive values for height and weight.")
