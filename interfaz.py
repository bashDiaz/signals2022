import streamlit as st
st.header("body", anchor=None)
opciones=["Hola","Adios","Cachon"]
st.selectbox("label", opciones, index=0, format_func=None,\
     key=None, help=None, on_change=None, args=None, kwargs=None,disabled=False)