import time
import streamlit as st
from streamlit_lottie import st_lottie_spinner

lottie_url = "https://lottie.host/97a3ad9b-b447-4994-a7f4-92ca1380d6b0/I7E9HUDnQh.json"

with st_lottie_spinner(lottie_url, key="unique_spinner_key"):
    time.sleep(5)

st.success("Processing complete!")
