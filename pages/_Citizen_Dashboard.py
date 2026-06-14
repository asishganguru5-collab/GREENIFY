
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

st.title("👤 Citizen Dashboard")
c1,c2,c3 = st.columns(3)

with c1:
    st.metric("GreenPoints","1250","+120")

with c2:
    st.metric("Waste Recycled","250 KG","+15")

with c3:
    st.metric("Sustainability Score","92%","+3")

st.divider()

st.subheader("♻️ Request Waste Pickup")

waste = st.selectbox(
    "Waste Type",
    ["Plastic","Paper","Metal","E-Waste","Glass"]
)

qty = st.number_input(
    "Quantity (KG)",
    min_value=1
)

address = st.text_area("Pickup Address")

if st.button("Book Pickup"):
    st.success("Pickup Scheduled Successfully!")