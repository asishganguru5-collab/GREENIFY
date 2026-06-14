import streamlit as st
st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#f0fff4,
#dcfce7,
#ffffff
);
}

[data-testid="stMetric"]{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

div.stButton > button{
background:linear-gradient(
90deg,
#22c55e,
#16a34a
);
color:white;
border:none;
border-radius:12px;
font-weight:bold;
padding:12px;
width:100%;
}

h1,h2,h3{
color:#166534;
}

</style>
""", unsafe_allow_html=True)
import pandas as pd
import plotly.express as px

st.title("📊 Greenify Analytics")

data = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Waste Collected": [120,180,250,320,400,520]
})

fig = px.line(
    data,
    x="Month",
    y="Waste Collected",
    title="Monthly Waste Collection"
)

st.plotly_chart(fig, use_container_width=True)

st.metric(
    "CO₂ Saved",
    "14 Tons"
)

st.metric(
    "Active Users",
    "4520"
)