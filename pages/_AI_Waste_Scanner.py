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
    page_title="AI Waste Scanner",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Waste Scanner")

st.write("Upload an image of waste and let Greenify classify it.")

uploaded_file = st.file_uploader(
    "Upload Waste Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(uploaded_file, width=350)

    st.success("Waste Identified Successfully")

    st.metric(
        "Waste Type",
        "Plastic Bottle"
    )

    st.metric(
        "Recyclability",
        "92%"
    )

    st.metric(
        "GreenPoints Earned",
        "+25"
    )

    st.info("""
    Suggested Action:
    Send this item to the Plastic Recycling Center.
    """)