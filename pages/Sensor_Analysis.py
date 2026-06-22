import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sensor Analysis",
    layout="wide"
)

st.title("📡 Sensor Analysis")

st.markdown("""
This module analyzes displacement and pore-pressure sensor data
to estimate landslide and rockfall risk.
""")

feature_df = pd.DataFrame({
    "Feature":[
        "displacement_mean",
        "pore_pressure_mean",
        "displacement_velocity",
        "pore_pressure_rate",
        "displacement_acceleration"
    ],
    "Importance":[
        0.615734,
        0.352334,
        0.020261,
        0.008472,
        0.003198
    ]
})

st.subheader("Feature Importance")

fig = px.bar(
    feature_df,
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Risk Distribution")

risk_df = pd.DataFrame({
    "Risk Class":["Low","Medium","High"],
    "Count":[23996,620,381]
})

fig2 = px.pie(
    risk_df,
    values="Count",
    names="Risk Class",
    hole=0.4
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader("Model Performance")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Accuracy","100%")

with col2:
    st.metric("Precision","99%")

with col3:
    st.metric("Recall","99%")

with col4:
    st.metric("F1 Score","99%")

st.subheader("Sensor Features Used")

st.write("""
• displacement_mean

• pore_pressure_mean

• displacement_velocity

• displacement_acceleration

• pore_pressure_rate
""")

st.subheader("Observations")

st.info("""
1. displacement_mean is the most influential feature.

2. pore_pressure_mean is the second most important feature.

3. High-risk events occur when displacement rapidly increases.

4. Sensor model provides the strongest contribution to final risk prediction.
""")