import streamlit as st
from utils.formatters import prettify
def show(result):
    if isinstance(result,dict):
        for k,v in result.items():
            if isinstance(v,(int,float,str)):
                st.metric(prettify(k),v)
            else:
                st.write(f"**{prettify(k)}**",v)
    else:
        st.write(result)
