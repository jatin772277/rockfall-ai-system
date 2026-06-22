import streamlit as st

st.title("About Project")

st.markdown("""
# AI-Based Rockfall Prediction & Early Warning System

This project predicts rockfall hazards in open-pit mines using:

- Sensor Data
- Terrain Data
- Weather Data

The system combines three machine learning models:

1. Sensor Risk Model
2. Terrain Risk Model
3. Weather Risk Model

These models generate a final risk score and provide
early warning alerts.
""")

st.subheader("Sensor Module")

st.write("""
Features Used:

- displacement_mean
- pore_pressure_mean
- displacement_velocity
- displacement_acceleration
- pore_pressure_rate
""")

st.subheader("Terrain Module")

st.write("""
Features Used:

- elevation
- slope
- aspect
- roughness
""")

st.subheader("Weather Module")

st.write("""
Features Used:

- rainfall
- temperature
- humidity
- wind speed
- pressure
""")