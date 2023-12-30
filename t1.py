import streamlit as st
import numpy as np
import time

st.header("Shapes Calculations")
st.sidebar.title("Configration")
with st.sidebar:
    shape=st.selectbox("Choose Shape",['Circle',"Rectanglar"])

if shape=="Circle":
    Rad=st.number_input("Radius:",max_value=100.0,min_value=0.0,step=0.01)
    area=Rad**2*np.pi
    perimeter=np.pi*2*Rad

if shape=="Rectanglar":
    Width=st.number_input("Width: ",max_value=100.0,min_value=0.0,step=0.1)
    height=st.number_input("Height: ",max_value=100.0,min_value=0.0,step=0.1)
    area=Width*height
    perimeter=(Width+height)*2

Calculations=st.button("Compute")
if Calculations:
    with st.spinner("Computing ....."):
        time.sleep(1)
        st.write("Area = ",area)
        st.write("Perieter = ",perimeter)
