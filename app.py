import streamlit as st

st.set_page_config(
    page_title="Greenify",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
background: linear-gradient(
135deg,
#f0fff4,
#dcfce7,
#ffffff
);
}

.hero{
padding:50px;
border-radius:25px;
background:white;
box-shadow:0px 10px 30px rgba(0,0,0,0.08);
text-align:center;
}

.big{
font-size:65px;
font-weight:800;
color:#16a34a;
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

st.markdown("""
<div class="hero">
<div class="big">🌱 Greenify</div>
<h2>Turning Waste Into Opportunity</h2>
<p>
A Circular Economy Platform Connecting Citizens,
Collectors and Recyclers
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Waste Recycled",
        "25,400 KG",
        "+12%"
    )

with c2:
    st.metric(
        "Citizens",
        "4,520",
        "+143"
    )

with c3:
    st.metric(
        "Collectors",
        "187",
        "+9"
    )

with c4:
    st.metric(
        "CO₂ Saved",
        "14 Tons",
        "+2.1"
    )

st.divider()

st.markdown("""
# 🌍 Greenify Impact Dashboard

### ♻️ 25,400 KG Waste Recycled

### 🌱 14 Tons CO₂ Saved

### 👥 4,520 Active Citizens

### 🚛 187 Waste Collectors

### 💰 ₹8.2 Lakhs Economic Value Generated
""")

st.divider()

st.markdown("""
## 🚀 Why Greenify?

Greenify transforms waste into economic opportunity.

### For Citizens
Earn GreenPoints for responsible waste disposal.

### For Waste Collectors
Get more pickup opportunities and earnings.

### For Recyclers
Access verified recyclable inventory through one platform.
""")

st.divider()

if st.button("🚀 Get Started"):
    st.switch_page("pages/_Login.py")