import streamlit as st
import pandas as pd

@st.cache_data(ttl=600)
def load_data(sheets_url):
  csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
  return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])
st.header('Biodata')

for row in df.itertuples():
  with st.container():
    st.subheader(f'Nama: {row.nama}')
    st.write(f'Umur: {row.umur}')
    st.write(f'Gender: {row.gender}')
    st.write(f'Pekerjaan: {row.pekerjaan}')