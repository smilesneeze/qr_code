import streamlit as st
import qrcode

st.title('QRコード生成アプリ')

url = st.text_input('QRコードを生成したいURL:')

if st.button('QRコード生成'):
    img = qrcode.make(url)
    st.image(img.get_image())