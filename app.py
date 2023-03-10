!pip install streamlit
!pip install protobuf==3.20.0

%%writefile app.py
import streamlit as st

st.title("Congratulations!")
st.header("You've just created a website")
st.balloons()
st.snow()

!streamlit run app.py & npx localtunnel --port 8501

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
radio = st.radio(label='Phép toán', options=('+', '-', 'x', ':'), horizontal=True)
b = st.number_input('Tham số b')
if a ==0:
    st.error('Phương trình vô nghiệm')
else: 
    st.success('Phương trình có 1 nghiệm', -b/a)