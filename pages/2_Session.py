import numpy as np
import streamlit as st 
import pandas as pd
import plotly.express as px

in1=st.text_input("Enter Some Text")
appnd=st.button("Append")
clr=st.button("Clear")
if "lis" not in st.session_state:
    st.session_state.lis=[]
if appnd:
    st.session_state.lis.append(in1)
if clr:
    st.session_state.lis=[]
st.write(st.session_state.lis)
st.write("Session_state",st.session_state)