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

st.title("🏆 GreenPoints Rewards")

st.metric(
    "Current Balance",
    "1250 Points"
)

st.subheader("Badges")

st.success("🥉 Bronze Recycler")
st.info("🥈 Silver Recycler")
st.warning("🥇 Gold Recycler")

st.subheader("Redeem Rewards")

if st.button("Redeem ₹50 Voucher"):
    st.success("Voucher Redeemed!")

if st.button("Redeem Coffee Coupon"):
    st.success("Coupon Redeemed!")