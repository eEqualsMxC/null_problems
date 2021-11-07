# Core pkgs
from __future__ import annotations
import pandas as pd
import streamlit as st
# import streamlit.components.v1 as components
import datetime
from datetime import date
from explorer import df_explorer
from home_layout import home_page



# Set page config
st.set_page_config(
    layout="wide",
    page_title='OSU Hackathon 2021',
    # initial_sidebar_state="collapsed",
    )

# App Utils
from PIL import Image






# ----------- Main Starts Here --------------------------------
def main():
    menu = ["Home","Upload Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        home_page()




    elif choice == "Upload Dataset":
        df_explorer()
            
        #     st.write(type(data_file))
        #     file_details = {"filename":data_file.name,
        #     "filetype":data_file.type,"filesize":data_file.size}
        #     st.write(file_details)
        #     df = pd.read_csv(data_file)
        #     st.dataframe(df)
    
    
if __name__ == '__main__':
    main()
