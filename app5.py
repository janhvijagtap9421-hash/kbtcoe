import streamlit as st

# Page config
st.set_page_config(page_title="Basic App")

# Add CSS
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    color: #2E86C1;
    font-size: 36px;
    font-weight: bold;
}

.result-box {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# Custom Title
st.markdown('<div class="title"> Welcome to Basic Streamlit App </div>', unsafe_allow_html=True)

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Nashik", "Pune"])

if st.button("Show Details"):
    st.markdown(f"""
    <div class="result-box">
        <h4>Your Details:</h4>
        <p><b>Age:</b> {age}</p>
        <p><b>City:</b> {city}</p>
    </div>
    """, unsafe_allow_html=True)