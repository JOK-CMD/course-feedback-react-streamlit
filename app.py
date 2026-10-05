import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="課程回饋", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
[data-testid="stHeader"] {display:none;}
.block-container {padding:0;max-width:100%;}
[data-testid="stMainBlockContainer"] {padding:0;}
iframe {border:0;}
</style>
""", unsafe_allow_html=True)
components.iframe("https://jok-cmd.github.io/course-feedback-react/", height=1100, scrolling=True)
