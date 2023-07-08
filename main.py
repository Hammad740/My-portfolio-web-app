import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_20220328_001502_882.jpg",width=450)

with col2:
    st.title("Mohammad Hammad")
    content = """ 


I am a skilled Python web developer, equipped with a deep understanding of web development frameworks and technologies.
 My expertise lies in utilizing Python to create dynamic and robust web applications. 
 With a strong grasp of both front-end and back-end development, I possess the ability to design and implement highly interactive user interfaces while seamlessly integrating them with efficient server-side logic."""
    st.info(content)
