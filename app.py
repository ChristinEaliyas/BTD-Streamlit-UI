
from enum import Enum
from io import BytesIO, StringIO
from typing import Union 
import pandas as pd
import streamlit as st
import os
from PIL import Image
def convertion(file, name):
    img = Image.open(file)
    gray_image = img.convert('L')
    return gray_image

def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.info(__doc__)
    html_code ="""
            <style>
            svg {
            visibility: hidden;
            }
            .row-widget stButton{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            }
            .css-1kyxreq etr89bj2{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            }
            .css-1n76uvr e1tzin5v0{
                height : 100%;
                width : 100%;
            }
            .css-esmr25 e1tzin5v0{
                height : 100%;
                width : 100%;
            }
            div .block-container css-1y4p8pa egzxvld4{
                height : 100%;
                width : 100%;
            }
            .container{
            height:100%;
            width:100%;
            }
            img {
                max-width: 100%;
            }
            .stAlert{
                display : none;
            }
            section .main-heading {
            position: relative;
            z-index: 1;
            margin: 0 auto;
            max-width: 500px;
            text-align: center;
            }
            section .main-heading h1 {
                color: orange;
            margin: 0;
            padding: 0;
            font-size: 3em;
            }
            section .main-heading p {
            font-size: 1.2em;
            }


            </style>
            <section class="design">
            <div class="main-heading">
            <h1 id="heading" class="text">Brain Tumor Detection</h1>
            <p>A brain tumor is a growth of cells in the brain or near it. Brain tumors can happen in the brain tissue. Brain tumors also can happen near the brain tissue.</p>
            </div>
            </section>
        """
    st.write(html_code, unsafe_allow_html=True)
 
    file = st.file_uploader("Upload file", type=["png", "jpg"], accept_multiple_files=False)
    show_file = st.empty()
    button_op = st.button('Scan',use_container_width=True)
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
        return
    content = file.getvalue()
    if button_op:
        with open(os.path.join("Uploaded_File",file.name),"wb") as f:
            f.write(file.getbuffer())
        gl_image = convertion(file, file.name)
        show_file.image(gl_image, use_column_width=True)
        button_download = st.download_button(label="Download", data=gl_image)
    
 
main()
