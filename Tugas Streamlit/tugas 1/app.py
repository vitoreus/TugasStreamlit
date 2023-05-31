import streamlit as st
import pandas as pd

# Linechart dengan dataframe yang dibuat manual
st.header("Penjualan Per Tahun")

df = pd.DataFrame({
  'year': ['2023', '2024', '2025', '2026', '2027'],
  'sales': [13000, 14000, 15000, 16000, 17000]
}, index=[1,2,3,4,5])

st.write('Tabel:')
st.dataframe(df, width=400)
st.markdown('#')

st.write('Linechart:')
st.line_chart(df, x='year')