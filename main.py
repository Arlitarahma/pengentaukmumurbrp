import streamlit as st

st.title("Aplikasi affah iyah")

taunskrg = st.number_input('Sekarang taun brp dik?')
taunlahir = st.number_input('Lahir taun brp dik?')

tombol = st.button('Umurku')

if tombol: 
    umur = taunskrg-taunlahir
    st.success(f'umurmu adalah {umur}')