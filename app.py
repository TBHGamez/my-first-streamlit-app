
import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if a ==0:
    st.error('Phương trình vô nghiệm')
else: 
    st.success(f'Phương trình có 1 nghiệm{-b/a}')
