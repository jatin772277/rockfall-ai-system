import streamlit as st
import pandas as pd
from datetime import datetime
import os
import plotly.graph_objects as go
from predict import *

st.set_page_config(page_title="AI RockFall Prediction System",layout="wide")

st.title("⛏️ AI-Based Rockfall Prediction & Alert System")
st.info("""
AI-Based Rockfall Prediction and Early Warning System

• Sensor Monitoring
• Terrain Analysis
• Weather Analysis

The system combines machine learning models from
sensor, terrain and weather modules to estimate
rockfall hazard levels.
""")
st.write("Predict rockfall risk using Sensor, Terrain, Weather Data.")

st.sidebar.header("Terrain Data")

elevation = st.sidebar.number_input("Elevation",value=2100.0)
slope = st.sidebar.number_input("Slope",value=45.0)
aspect = st.sidebar.number_input("Aspect",value=120.0)
roughness = st.sidebar.number_input("Roughness",value=80.0)

st.sidebar.header("Weather Data")

rainfall = st.sidebar.number_input("Rainfall (7 Days)",value=35.0)
temperature = st.sidebar.number_input("Temperature",value=20.0)
humidity = st.sidebar.number_input("Humidity",value=85.0)
wind = st.sidebar.number_input("Wind Speed",value=5.0)
pressure = st.sidebar.number_input("Pressure",value=82.0)

st.sidebar.header("Sensor Data")

displacement = st.sidebar.number_input("Displacement Mean",value=0.4)
pore_pressure = st.sidebar.number_input("Pore Pressure Mean",value=4.2)
velocity = st.sidebar.number_input("Displacement Velocity",value=0.03)
acceleration = st.sidebar.number_input("Displacement Acceleration",value=0.002)
pressure_rate = st.sidebar.number_input("Pore Pressure Rate",value=0.05)

if st.button("Predict Risk"):

    terrain_input = [elevation,slope,aspect,roughness]
    weather_input = [rainfall,temperature,humidity,wind,pressure]
    sensor_input = [displacement,pore_pressure,velocity,acceleration,pressure_rate]

    result = predict_final_risk(
        terrain_input,
        weather_input,
        sensor_input
    )

    risk_level = risk_category(result["final"])

    st.subheader("Results")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Final Risk",result["final"])

    with col2:
        st.metric("Sensor Risk",result["sensor"])

    with col3:
        st.metric("Terrain Risk",result["terrain"])

    with col4:
        st.metric("Weather Risk",result["weather"])

    new_row = pd.DataFrame([{
        "TimeStamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Terrain Risk": result["terrain"],
        "Weather Risk": result["weather"],
        "Sensor Risk": result["sensor"],
        "Final Risk": result["final"],
        "Risk Level": risk_level
    }])

    if os.path.exists("data/prediction_logs.csv"):
        old_df = pd.read_csv("data/prediction_logs.csv")
        log_df = pd.concat([old_df,new_row],ignore_index=True)
    else:
        log_df = new_row

    log_df.to_csv(
        "data/prediction_logs.csv",
        index=False
    )

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=result["final"],
        title={"text":"Final Risk Score"},
        gauge={
            "axis":{"range":[0,1]},
            "steps":[
                {"range":[0,0.3],"color":"lightgreen"},
                {"range":[0.3,0.6],"color":"gold"},
                {"range":[0.6,1],"color":"salmon"}
            ]
        }
    ))

    fig.update_layout(height=400)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if risk_level == "HIGH":

        st.error("🚨 HIGH ROCKFALL RISK")

        st.markdown("""
### Recommended Actions

- Evacuate workers from high-risk zones
- Suspend blasting activities
- Increase monitoring frequency
- Conduct slope stability inspection
""")

    elif risk_level == "MEDIUM":

        st.warning("⚠ MODERATE ROCKFALL RISK")

    else:

        st.success("✅ LOW ROCKFALL RISK")


if os.path.exists("data/prediction_logs.csv"):

    st.subheader("Recent Predictions")

    history = pd.read_csv(
        "data/prediction_logs.csv"
    )

    st.dataframe(
        history.tail(10),
        use_container_width=True
    )

    with open(
        "data/prediction_logs.csv",
        "rb"
    ) as file:

        st.download_button(
            label="📥 Download Prediction Report",
            data=file,
            file_name="prediction_logs.csv",
            mime="text/csv"
        )

st.markdown("---")

st.caption(
    "Developed using Sensor, Terrain and Weather-based ML Models"
)