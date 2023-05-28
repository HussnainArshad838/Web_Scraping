import streamlit as st
import requests
pip install beautifulsoup4
from bs4 import BeautifulSoup
import webbrowser

st.markdown("<h1 style='text-align:center;'>Web Scraping</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")
    placeholder = st.empty()

    if keyword:
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'html.parser')  # Changed parser to 'html.parser'
        rows = soup.find_all("div", class_="ripi6")  # Updated the class name
        col1, col2 = placeholder.columns(2)
        
        for index, row in enumerate(rows):
            figures = row.find_all("figure")
            
            for i in range(2):
                img = figures[i].find("img", class_="YVj9w")
                image_list = img["srcset"].split("?")
                anchor = figures[i].find("a", class_="rEAWd")
                
                if i == 0:
                    col1.image(image_list[0])
                    btn = col1.button("Download", key=str(index)+str(i))
                    if btn:
                        webbrowser.open_new_tab("https://unsplash.com/s" + anchor["href"])
                else:
                    col2.image(image_list[0])
                    btn = col2.button("Download", key=str(index)+str(i))
                    if btn:
                        webbrowser.open_new_tab("https://unsplash.com" + anchor["href"])
                
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









