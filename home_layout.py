import streamlit as st
import streamlit.components.v1 as components

# App Utils
from PIL import Image

# Home Lay Out
def home_page():
    row1_cols = st.columns(2)

    with row1_cols[0]:
        with st.container():
            st.write(
            """
            ### **Veeva Systems: Ohio State Hackathon 2021**
            """) 

            st.write(
            """
            The pharmaceutical industry uses prescriber data to target doctors with life-saving medications and therapies.
            Companies can use the prescriber data to help understand how doctors prescribe their product, as well as helping 
            them to track total prescriptions (TRx) and new prescriptions (NRx) for a product in a given market 🍁.  
            """)
            st.write(
            """
             
            """)

            st.markdown('#### Import Links 💻')
            st.markdown('OSU Hackathon: [Hack Here](https://hack.osu.edu/2021/ "I need work").')
            st.markdown('Hack Instructions: [Goto PDF](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/viewer.html?pdfurl=https%3A%2F%2Fhack.osu.edu%2F2021%2Flive%2Fassets%2Fchallenges%2FVeeva-Systems_Challenge.pdf&clen=98393 "I need work").')
            st.markdown('Resume: [Linkedin/mustaine](www.linkedin.com/in/justin-mustaine-84b5a71aa "I need work").')
            st.write(
            """
     
            """)



        img_01 = Image.open("images/Hackathon.png")
        st.image(img_01)
        
    with row1_cols[1]:
        
        img_02 = Image.open("images/veeva_icon.png")
        st.image(img_02)
    

    st.write(
            """

            #### Citations 📝
            """)
    st.markdown('Language 1: [Python 3.9](https://www.python.org/downloads/release/python-390/).')
    st.markdown('Language 2: [Markdown](https://project-awesome.org/BubuAnabelas/awesome-markdown).')
    st.markdown('Frame Work: [Streamlit.io](https://streamlit.io/).')
    st.markdown('Data Analysis Pkg 1: [Pandas](https://pandas.pydata.org/).')
    st.markdown('Data Analysis Pkg 2: [Numpy](https://numpy.org/).')
    st.markdown('Data Viz: [Plotly](https://plotly.com/).')
    st.write(
    """
    """)

