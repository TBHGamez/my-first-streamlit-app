import pickles
import streamlit as st
import sklearn

filename = 'model.pickle'


model = pickles.load(open(filename, "rb"))
st.balloons()
y_pred = model.predict(x)
ii= mae(y, y_pred)

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
#x_new = st.number_input('blabla')
#y_new = model.predict(x_new)

if st.button('Giải'):
    st.success(f'{ii}')
        




