import pickle
import streamlit as st
import sklearn
model = pickle.load(open(filename, "rb"))
st.balloons()

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
x_new = st.number_input('blabla')
y_new = model.predict(x_new)

if st.button('Giải'):
    st.success(f'{y_new}')
        




