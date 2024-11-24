import streamlit as st
import os
from src.pipeline import rag_pipeline,qa_pipeline
import time

# folder for file save
if not os.path.exists("data"):
    os.makedirs("data",exist_ok=True)

# initialize session
if "isdoc" not in st.session_state.keys():
    st.session_state.isdoc = False

## file upload 
file = st.sidebar.file_uploader("Upload the file.",type=["pdf","docx"])

if st.sidebar.button("Submit") and file != None:
    file_path = os.path.join("data",file.name)
    with open(file_path,'wb') as f:
        f.write(file.getbuffer())
    db_name = os.path.join("vec_db",file.name)
    if not os.path.exists(db_name):
        pipeline = rag_pipeline(filepath=file_path,db_path=db_name)
        if pipeline == True:
            st.session_state.isdoc = db_name
            st.sidebar.success("Vector Database Created.")
        else:
            st.error(pipeline)
    elif not os.path.exists(db_name):
        st.session_state.isdoc = db_name

else:
    st.sidebar.warning("Please Upload file.")


## Chat bot
if st.session_state.isdoc:
    if "message" not in st.session_state.keys():
        st.session_state.message  =  [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

    for message in st.session_state.message:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.message.append({"role":"user","content":prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.message[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking"):
                response = qa_pipeline(db_path=st.session_state.isdoc,query=prompt)
                st.write(response)
            
            message = {"role":"assistant","content":response}
            st.session_state.message.append(message)

else:
    st.warning("Please upload document in sidebar")