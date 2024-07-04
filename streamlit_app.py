import streamlit as st
import pandas as pd
st.title("hello")
res=st.text_input("play with me:")
st.write("you entered:",res)
rt=pd.read_csv("car_prices.csv")
sd.line_chart(rt)
