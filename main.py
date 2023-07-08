import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_20220328_001502_882.jpg")

with col2:
    st.title("Mohammad Hammad")
    content = """ 


I am a skilled Python web developer, equipped with a deep understanding of web development frameworks and 
technologies. My expertise lies in utilizing Python to create dynamic and robust web applications. With a strong 
grasp of both front-end and back-end development, I possess the ability to design and implement highly interactive 
user interfaces while seamlessly integrating them with efficient server-side logic. """
    st.info(content)

content2 = """Below  you can find some of the apps I have build in Python.Feel free to contact me !"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/" + rows["image"])
        # st.write("[Source Code](https://github.com/Hammad740/My-Todo-Web-App/tree/master)")
        st.write(f"[Source Code]({rows['url']})")
with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/" + rows["image"])
        # st.write("[Source Code](https://github.com/Hammad740/My-Todo-Web-App/tree/master)")
        st.write(f"[Source Code]({rows['url']})")
