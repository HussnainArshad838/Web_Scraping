import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align:center;'>Web Scraping</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")

    if search:
        col1, col2 = st.columns(2)
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'html.parser')  # Changed parser to 'html.parser'
        rows = soup.find_all("div", class_="ripi6")  # Updated the class name

        for row in rows:
            figures = row.find_all("figure")
            for i in range(2):
                img = figures[i].find("img", class_="YVj9w")
                image_list = img["srcset"].split("?")
                if i == 0:
                    col1.image(image_list[0])
                else:
                    col2.image(image_list[0])
                st.image(image_list[0])
                 


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









