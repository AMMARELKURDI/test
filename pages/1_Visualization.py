import numpy as np
import streamlit as st 
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data(file):
    return(pd.read_csv(file))

file=st.file_uploader("Upload Your File",type=["csv","xlsx"])

if file is not None:
    df=load_data(file)

    num_row=st.slider("Choose Num Of Rows:",max_value=len(df),min_value=1,step=1)
    Selecting_Columns=st.multiselect("Select Columns",options =df.columns.to_list(),default=df.columns.to_list())
    st.write(df[:num_row][Selecting_Columns])
    df=df[:num_row][Selecting_Columns]

    numeric_col=df.select_dtypes(include=np.number).columns.to_list()
    string_col=df.select_dtypes(include="object",exclude='datetime').columns.to_list()

    t1,t2=st.tabs(["Scatter","Histogram"])
    with t1:

        c1,c2,c3,c4=st.columns(4)
        with c1:
            x_col=st.selectbox("Select X-Axis",numeric_col)
        with c2:
            y_col=st.selectbox("Select Y-Axis",numeric_col)
        with c3:
            numeric_col.append(None)
            size_Bubble=st.selectbox("Select Bubble Size",numeric_col)
        with c4:
            string_col.append(None)
            clor=st.selectbox("Select Bubble Color",string_col)

        fig_scatter=px.scatter(df,x=x_col,y=y_col,color=clor,size=size_Bubble)
        st.plotly_chart(fig_scatter)
    with t2:
        hist_col=st.selectbox("Select Histogram Category",numeric_col)
        fig_hist=px.histogram(df,x=hist_col)
        st.plotly_chart(fig_hist)



    
    

    