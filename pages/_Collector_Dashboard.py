
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
if st.button("🚪 Logout"):
    st.switch_page("pages/_Login.py")

st.title("🚛 Collector Dashboard")

c1,c2,c3 = st.columns(3)

c1.metric("Today's Pickups","18","+3")
c2.metric("Earnings","₹2,450","+400")
c3.metric("Efficiency","96%","+2")

st.divider()

st.subheader("Pending Pickups")

st.info("Plastic Waste - 12 KG")
st.info("Paper Waste - 20 KG")
st.info("E-Waste - 5 KG")