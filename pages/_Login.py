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

st.set_page_config(
    page_title="Greenify Login",
    page_icon="🌱",
    layout="wide"
)

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

</style>
""", unsafe_allow_html=True)

st.title("🌱 Greenify Login")

role = st.selectbox(
    "Select Role",
    [
        "Citizen",
        "Waste Collector",
        "Recycler"
    ]
)

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login", use_container_width=True):

    if role == "Citizen":
        st.switch_page(
            "pages/_Citizen_Dashboard.py"
        )

    elif role == "Waste Collector":
        st.switch_page(
            "pages/_Collector_Dashboard.py"
        )

    else:
        st.switch_page(
            "pages/_Recycler_Dashboard.py"
        )
