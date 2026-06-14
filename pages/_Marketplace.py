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

st.title("♻️ Recycling Marketplace")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Plastic Waste")
    st.write("120 KG Available")
    st.write("₹20 / KG")
    st.button("Buy", key="plastic")

with col2:
    st.success("Paper Waste")
    st.write("200 KG Available")
    st.write("₹10 / KG")
    st.button("Buy", key="paper")

with col3:
    st.success("Metal Waste")
    st.write("80 KG Available")
    st.write("₹35 / KG")
    st.button("Buy", key="metal")