import streamlit as st
import math

# Title of the app
st.title("Circle Area Calculator")

# User input for radius
radius = st.number_input("Enter the radius of the circle:", min_value=0.0, format="%.2f")

# Button to calculate area
if st.button("Calculate Area"):
    area = math.pi * radius ** 2
    st.success(f"The area of the circle is: {area:.2f} square units.")
