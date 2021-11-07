# Core pkgs
from __future__ import annotations
import pandas as pd
from pandas.core.frame import DataFrame
import streamlit as st
import re

# Data Viz
import plotly.graph_objects as go
import plotly.express as px



# App Utils
from PIL import Image

# Plot custom Pkgs
from plots import count_hist, count_hist_custom, map_it

# utils
# import base64
# import time
# timestr = time.strftime("%Y%m%d-%H%M%S")


@st.cache(show_spinner=True)
def load_data(data_file):
        """Load in csv"""
        return pd.read_csv(data_file)



# ----------- Main Starts Here --------------------------------
def df_explorer():
        
        month_num_dict = {
                '1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'
        }
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV",type=["csv"])
        if data_file is not None:
                
                st.session_state.df_data = pd.read_csv(data_file)
                st.session_state.nrx_names = [nrx for nrx in list(st.session_state.df_data.columns)[5:] if nrx[:3] == 'NRx']
                st.session_state.trx_names = [trx for trx in list(st.session_state.df_data.columns)[5:] if trx[:3] == 'TRx']

                # State total perscriptions
                unique_states = st.session_state.df_data['State'].value_counts().rename_axis('State').reset_index(name='Count').reset_index(drop=True)

                # State Total Nrx
                temp_nrx = ['id','first_name','last_name','State','Product'] + st.session_state.nrx_names
                st.session_state.NRX =  st.session_state.df_data[temp_nrx]
                state_nrx = st.session_state.NRX.groupby(['State'])[st.session_state.nrx_names].apply(lambda x : x.astype(int).sum())
                state_nrx = state_nrx.reset_index(drop=False)
                state_nrx["sum"] = state_nrx[st.session_state.nrx_names].sum(axis=1)
                state_nrx.rename(columns={'sum': 'Count'}, inplace=True)
                unique_state_nrx =  state_nrx[['State','Count']].sort_values(by='Count', ascending=False)


                # State Total Trx
                temp_trx = ['id','first_name','last_name','State','Product'] + st.session_state.trx_names
                st.session_state.TRX =  st.session_state.df_data[temp_trx]
                state_trx = st.session_state.TRX.groupby(['State'])[st.session_state.trx_names].apply(lambda x : x.astype(int).sum())
                state_trx = state_trx.reset_index(drop=False)
                state_trx["sum"] = state_trx[st.session_state.trx_names].sum(axis=1)
                state_trx.rename(columns={'sum': 'Count'}, inplace=True)
                unique_state_trx =  state_trx[['State','Count']].sort_values(by='Count', ascending=False)

                # Make a state dictionary
                us_state_abbrev = {
                'Alabama': 'AL',
                'Alaska': 'AK',
                'American Samoa': 'AS',
                'Arizona': 'AZ',
                'Arkansas': 'AR',
                'California': 'CA',
                'Colorado': 'CO',
                'Connecticut': 'CT',
                'Delaware': 'DE',
                'District of Columbia': 'DC',
                'Florida': 'FL',
                'Georgia': 'GA',
                'Guam': 'GU',
                'Hawaii': 'HI',
                'Idaho': 'ID',
                'Illinois': 'IL',
                'Indiana': 'IN',
                'Iowa': 'IA',
                'Kansas': 'KS',
                'Kentucky': 'KY',
                'Louisiana': 'LA',
                'Maine': 'ME',
                'Maryland': 'MD',
                'Massachusetts': 'MA',
                'Michigan': 'MI',
                'Minnesota': 'MN',
                'Mississippi': 'MS',
                'Missouri': 'MO',
                'Montana': 'MT',
                'Nebraska': 'NE',
                'Nevada': 'NV',
                'New Hampshire': 'NH',
                'New Jersey': 'NJ',
                'New Mexico': 'NM',
                'New York': 'NY',
                'North Carolina': 'NC',
                'North Dakota': 'ND',
                'Northern Mariana Islands':'MP',
                'Ohio': 'OH',
                'Oklahoma': 'OK',
                'Oregon': 'OR',
                'Pennsylvania': 'PA',
                'Puerto Rico': 'PR',
                'Rhode Island': 'RI',
                'South Carolina': 'SC',
                'South Dakota': 'SD',
                'Tennessee': 'TN',
                'Texas': 'TX',
                'Utah': 'UT',
                'Vermont': 'VT',
                'Virgin Islands': 'VI',
                'Virginia': 'VA',
                'Washington': 'WA',
                'West Virginia': 'WV',
                'Wisconsin': 'WI',
                'Wyoming': 'WY'
                }
                
                st.session_state.df_data['state_abbrev'] = st.session_state.df_data['State'].replace(us_state_abbrev)
       

                with st.expander(f"DataFrame"):
                       
                        st.dataframe(st.session_state.df_data)

                with st.expander(f"Distributions: State"):

                        with st.container():
                                st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40","Unique States Observed"),unsafe_allow_html=True)
                                fig = count_hist(df=unique_states, x='State', y='Count')
                                st.plotly_chart(fig,use_container_width=True)

                                st.markdown(
                                        """
                                        ***
                                        """)
                        with st.container():

                                st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40","Total prescriptions (TRx) Count by state"),unsafe_allow_html=True)
                                fig = count_hist(df=unique_state_trx, x='State', y='Count')
                                st.plotly_chart(fig,use_container_width=True)
                        
                                unique_state_trx['state_abbrev'] = unique_state_trx['State'].replace(us_state_abbrev)
                                unique_state_trx_temp  = unique_state_trx[['state_abbrev','Count']]
                                fig = map_it(unique_state_trx_temp, 'state_abbrev', 'Count')
                                st.plotly_chart(fig,use_container_width=True)
                

                                st.markdown(
                                        """
                                        ***
                                        """)
                        with st.container():

                                st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40","New prescriptions (NRx) Count by state"),unsafe_allow_html=True)
                                fig = count_hist(df=unique_state_nrx, x='State', y='Count')
                                st.plotly_chart(fig,use_container_width=True)

                                unique_state_nrx['state_abbrev'] = unique_state_nrx['State'].replace(us_state_abbrev)
                                unique_state_nrx_temp  = unique_state_nrx[['state_abbrev','Count']]
                                fig = map_it(unique_state_nrx_temp, 'state_abbrev', 'Count')
                                st.plotly_chart(fig,use_container_width=True)
                        
                with st.expander(f"Distributions: NRx Months"):
                        
                        with st.container():
                                @st.cache(show_spinner=True)
                                def get_nrx_month(month):
                                                temp_frame = state_nrx[['State',f"{name}"]]
                                                temp_frame.rename(columns={f"{name}": f"{month}"}, inplace=True)
                                                temp_frame =  temp_frame[['State',f"{month}"]].sort_values(by=f"{month}", ascending=False)
                                                return temp_frame
                                
                                for name in st.session_state.nrx_names:
                                        temp_frame = None
                                        month = ''
                                        if name[-2] != '11' or name[-2] != '12':
                                                month = month_num_dict[name[-1:]]
                                        else:
                                                month = month_num_dict[name[-2:]]
                                        
                                        temp_frame = get_nrx_month(month)

                                        st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40",f"{month} NRx Count by State"),unsafe_allow_html=True)
                                        fig = count_hist_custom(df=temp_frame, x='State', y=f"{month}",label=('State', f'{month} Count NRx'))
                                        st.plotly_chart(fig,use_container_width=True)
                                
                                st.markdown(
                                        """
                                        ***
                                        """)
                                st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40",f"(%) NRx Change by Month and grouped by State"),unsafe_allow_html=True)

                                
                                tail_month =st.session_state.nrx_names[0]
                                monthly_list_prep = []

                                for name in st.session_state.nrx_names[1:]:
                                        monthly_list_prep.append([tail_month,name])
                                        tail_month = name
                                
                                for group in monthly_list_prep:
                                        temp_frame_pct = state_nrx[['State',f"{group[0]}",f"{group[1]}"]]
                                        temp_frame_pct[f'{group[1]} D'] = temp_frame_pct[[f"{group[0]}",f"{group[1]}"]].pct_change(axis=1)[f"{group[1]}"]

                                        month = ''
                                        if group[1][-2] != '11' or group[1][-2] != '12':
                                                month = month_num_dict[name[-1:]]
                                        else:
                                                month = month_num_dict[name[-2:]]
              
                                        temp_frame_pct.rename(columns={f'{group[1]} D': f"{month} % Change"}, inplace=True)
                                        # temp_frame_pct =  temp_frame_pct[['State',f"{month} % Change"]].sort_values(by=f"{month} % Change", ascending=False)
                                        temp_frame_pct =  temp_frame_pct[['State',f"{month} % Change"]]
                                     


                                        st.markdown(
                                        """
                                        ***
                                        """)

                                        st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40",f"{month} NRx % Δ"),unsafe_allow_html=True)
                                        fig = count_hist_custom(df=temp_frame_pct, x='State', y=f"{month} % Change",label=('State', f'NRx {month} % Δ'))
                                        st.plotly_chart(fig,use_container_width=True)               
                                
                with st.expander(f"Distributions: TRx Months"):
                        with st.container():
                                @st.cache(show_spinner=True)
                                def get_trx_month(month):
                                                temp_frame = state_trx[['State',f"{name}"]]
                                                temp_frame.rename(columns={f"{name}": f"{month}"}, inplace=True)
                                                temp_frame =  temp_frame[['State',f"{month}"]].sort_values(by=f"{month}", ascending=False)
                                                return temp_frame
                                
                                for name in st.session_state.trx_names:
                                        temp_frame = None
                                        month = ''
                                        if name[-2] != '11' or name[-2] != '12':
                                                month = month_num_dict[name[-1:]]
                                        else:
                                                month = month_num_dict[name[-2:]]
                                        
                                        temp_frame = get_trx_month(month)

                                        st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40",f"{month} TRx Count by State"),unsafe_allow_html=True)
                                        fig = count_hist_custom(df=temp_frame, x='State', y=f"{month}",label=('State', f'{month} Count TRx'))
                                        st.plotly_chart(fig,use_container_width=True)
                                
                                st.markdown(
                                        """
                                        ***
                                        """)
                                st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40",f"(%) TRx Change by Month and grouped by State"),unsafe_allow_html=True)

                                
                                tail_month =st.session_state.trx_names[0]
                                monthly_list_prep = []

                                for name in st.session_state.trx_names[1:]:
                                        monthly_list_prep.append([tail_month,name])
                                        tail_month = name
                                
                                temp_frame_pct =None
                                for group in monthly_list_prep:
                                        temp_frame_pct = state_trx[['State',f"{group[0]}",f"{group[1]}"]]
                                        temp_frame_pct[f'{group[1]} D'] = temp_frame_pct[[f"{group[0]}",f"{group[1]}"]].pct_change(axis=1)[f"{group[1]}"]

                                        month = ''
                                        st.write(group[1][-2])
                                        if group[1][-2] != '11' or group[1][-2] != '12':
                                                month = month_num_dict[group[1][-1:]]
                                        else:
                                                month = month_num_dict[group[1][-2:]]
              
                                        temp_frame_pct.rename(columns={f'{group[1]} D': f"{month} % Change"}, inplace=True)
                                        # temp_frame_pct =  temp_frame_pct[['State',f"{month} % Change"]].sort_values(by=f"{month} % Change", ascending=False)
                                        temp_frame_pct =  temp_frame_pct[['State',f"{month} % Change"]]
                                     


                                        st.markdown(
                                        """
                                        ***
                                        """)

                                        st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","40",f"{month} TRx % Δ"),unsafe_allow_html=True)
                                        fig = count_hist_custom(df=temp_frame_pct, x='State', y=f"{month} % Change",label=('State', f'TRx {month} % Δ'))
                                        st.plotly_chart(fig,use_container_width=True)
                
                
                with st.expander(f"Distributions: Top Products (TRx) and Doctors"):

                        temp_trx = st.session_state.df_data[['first_name','last_name','Product']+st.session_state.trx_names]
                        unique_drugs = temp_trx.Product.unique().tolist()

                        for drug in unique_drugs:

                                temp_df = temp_trx[temp_trx.Product==str(drug)]
                                st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("red","40",f"Monthly top doctors with {drug.title()} prescriptions: "),unsafe_allow_html=True)
                                # st.markdown(f"#### Monthly top doctors with {drug.title()} prescriptions: ")

                                for name in st.session_state.trx_names:
                                        
                                        tdf=temp_df[['first_name','last_name','Product', name]].sort_values(by=name, ascending=False)
                                        tdf = [str(x) for x in tdf.iloc[0,:]]
                                        tdf.append(month_num_dict[name.split("_",2)[-1]])


                                        st.markdown("***")
                                        st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","20",f"Drug: {tdf[2]}, Month: {tdf[4]}, Qty: {tdf[3]}"),unsafe_allow_html=True)
                                        st.markdown("\
                                        <h1 style='text-align: center; \
                                        font-weight: 1000;\
                                        color: {}; \
                                        font-size:{}px;'>{}</h1>\
                                        ".format("blue","20",f"First Name: {tdf[0]}, Last Name: {tdf[1]}"),unsafe_allow_html=True)
                                        
                                        # st.markdown(f"##### Drug: {tdf[2]}, Month: {tdf[4]}, Qty: {tdf[3]}")
                                        # st.markdown(f"##### First Name: {tdf[0]}, Last Name: {tdf[1]}")
                                        st.markdown("***")
                                        st.markdown(" ")
                
                with st.expander(f" : NRx Forcast"):
                        pass
                            

                                   

                                        
                                        
                           
                                     




                

                        
                   
     
                        
                



if __name__ == '__df_explorer__':
    df_explorer()