import time
import streamlit as st
from streamlit_lottie import st_lottie

# Load the Lottie animation
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"

# Display the Lottie animation
lottie_placeholder = st.empty()
with lottie_placeholder:
    st_lottie(lottie_url, key="unique_key_for_lottie")

# Simulate some processing time
with st.spinner("Processing..."):
    time.sleep(5)

# Clear the Lottie animation after processing
lottie_placeholder.empty()

st.success("Processing complete!")
