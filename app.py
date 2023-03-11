
import streamlit as st
import sklearn
import plotly
st.balloons()
st.snow()
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if a ==0:
    st.error('Phương trình vô nghiệm')
else: 
    st.success(f'Phương trình có 1 nghiệm{-b/a}')
