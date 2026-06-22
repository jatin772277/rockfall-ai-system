import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Weather Analysis",
    layout="wide"
)

st.title("🌦️ Weather Analysis")

weather_stats = pd.DataFrame({
    "Feature":[
        "Temperature",
        "Humidity",
        "Rainfall",
        "Wind Speed",
        "Pressure"
    ],
    "Mean":[
        9.91,
        54.25,
        1.33,
        1.91,
        82.52
    ]
})

st.subheader("Weather Statistics")

st.dataframe(
    weather_stats,
    use_container_width=True
)

fig = px.bar(
    weather_stats,
    x="Feature",
    y="Mean",
    text="Mean"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Weather Risk Summary")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Weather Alerts",
        "9"
    )

with col2:
    st.metric(
        "Normal Days",
        "1812"
    )

with col3:
    st.metric(
        "Alert Ratio",
        "0.49%"
    )

risk_df = pd.DataFrame({
    "Class":["Normal","Alert"],
    "Count":[1812,9]
})

fig2 = px.pie(
    risk_df,
    values="Count",
    names="Class",
    hole=0.4
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader("Important Weather Factors")

st.write("""
• Rainfall Accumulation (3 Day)

• Rainfall Accumulation (7 Day)

• Humidity Change

• Temperature Change

• Pressure Change
""")

st.info("""
1. Heavy rainfall increases slope instability.

2. Continuous rainfall raises pore pressure.

3. Sudden weather changes can accelerate failure.

4. Weather contributes 30% of the final risk score.
""")