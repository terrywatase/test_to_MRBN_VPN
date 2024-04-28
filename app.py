import streamlit as st
import os

st.title("Filemanagement")

folder_path ="\\\\inet\\PUB\\D2320_ディオネカンパニー\\D2321_ディオネカンパニー_HT課"

try: 
      file_names = os.listdir(folder_path)
      st.write(file_names) 
except:
      st.markdown("""
                  ### 社外アクセスの場合、VPNが必要です
                   """)


