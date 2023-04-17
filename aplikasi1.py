import streamlit as st

#Judul
st.title('ini test aja, eh keknya buat lu dah')
st.subheader('keknya bener buat lu deh')
st.write('coba masukkin kode yang tertera deh, kalo kodenya salah bukan lu orangnya WKWKWK')

#Input Code
code = st.number_input('masukkin kodenya deh')
st.write('kodenya',code)

#hasil
number = code*1
st.button('coba ah')

if number==24012004:
    st.write('cie nyoba')
elif number<=24012004:
    st.write('maaf coba lagi cek angkanya')
else:
    st.write('kamu siapa')
        
