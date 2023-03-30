# Import the libraries
import streamlit as st
import pandas as pd
import numpy as np

# Set up the configuration of the page
st.set_page_config(page_title="File uploader",
                   page_icon=":open_file_folder:",
                   initial_sidebar_state="expanded",
                   menu_items={
                    "Get help":"mailto:audedako@gmail.com",
                    "Report a bug":"mailto:audedako@gmail.com",
                    "About":"This app is just a self tuto as training. Its purpose is to develop personal skills."
                   })