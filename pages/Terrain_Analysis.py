import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Terrain Analysis",
    layout="wide"
)

st.title("🗻 Terrain Analysis")

terrain_stats = pd.DataFrame({
    "Feature":["Elevation","Slope","Aspect","Roughness"],
    "Mean":[1971.14,19.15,164.68,29.75],
    "Max":[2420.72,61.83,359.99,157.48]
})

st.subheader("Terrain Statistics")

st.dataframe(
    terrain_stats,
    use_container_width=True
)

st.subheader("Terrain Feature Distribution")

fig = px.bar(
    terrain_stats,
    x="Feature",
    y="Mean",
    text="Mean"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Terrain Risk Summary")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Mean Terrain Risk",
        "0.326"
    )

with col2:
    st.metric(
        "Max Terrain Risk",
        "0.892"
    )

with col3:
    st.metric(
        "Alert Locations",
        "183"
    )

st.subheader("Risk Distribution")

risk_df = pd.DataFrame({
    "Class":["Normal","Alert"],
    "Count":[30205,183]
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

st.subheader("Observations")

st.info("""
1. High slope values significantly increase terrain risk.

2. Rough terrain contributes to instability.

3. 183 terrain alert locations were identified.

4. Terrain risk contributes 30% of the final risk score.
""")