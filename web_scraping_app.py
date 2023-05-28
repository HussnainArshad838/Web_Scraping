import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align:center;'>Web Scraping</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")

    if search:
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'html.parser')  # Changed parser to 'html.parser'
        rows = soup.find_all("div", class_="_2VWD4 _2zEKz")  # Updated the class name

        for row in rows:
            # Perform further processing on each row as needed
            pass

#import streamlit as st
#import requests
#from bs4 import BeautifulSoup

#st.markdown("<h1 style='text-align:center;'>Web Scraping</h1>", unsafe_allow_html=True)

#with st.form("Search"):
   # keyword = st.text_input("Enter Your Keyword")
   # search = st.form_submit_button("Search")
    
  #  if search:
   #     page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    #    soup=Beautifulsoup(page.content,'lxml')
    #    rows=soup.find_all("div",class_="ripi6")









