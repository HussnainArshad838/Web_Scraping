import streamlit as st
import requests
from bs4 import Beautifulsoup
st.markdown("<h1 style='text-align:center;'>Web Scraping </h1>",unsafe_allow_html=True)
with st.form("Search"):
    keyword=st.text_input("Enter Your Keyword")
    Search=st.form_submit_button("Search")
    if Search:
        page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
        print(page.status_code)








