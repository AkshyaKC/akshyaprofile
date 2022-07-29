import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('aks.jpg'))

st.header('Akshya Kumar KC')

st.info('Data Analyst/Science Practitioner')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/akshya-kumar-kc-2ab404170/', 'Follow me on LinkedIn', icon_size)
st_button('twitter', 'https://twitter.com/AkshyaKKC', 'Follow me on Twitter', icon_size)
st_button('instagram', 'https://www.instagram.com/cristiano/?hl=en', 'Follow me on Instagram', icon_size)
st_button('medium', 'https://medium.com/@akshyakc095', 'Read my Blogs', icon_size)
