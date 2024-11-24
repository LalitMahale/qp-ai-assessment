import streamlit as st




## file upload 

file = st.sidebar.file_uploader("Upload the file.",type=["pdf","docx"])
if file != None:
    st.sidebar.write(file.name)



