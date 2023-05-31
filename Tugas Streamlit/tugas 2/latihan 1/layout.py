import streamlit as st
import pandas as pd
import numpy as np

# Layout Column
st.header('Sales Data')

np.random.seed(100)
df = pd.DataFrame({
  'Tahun': ['2023', '2024', '2025', '2026', '2027'],
  'Produk1': np.random.randint(100, 1000, 5),
  'Produk2': np.random.randint(100, 1000, 5),
  'Produk3': np.random.randint(100, 1000, 5)
  }, index=[1,2,3,4,5])

col1, col2 = st.columns(2)
with col1:
  st.subheader('Tabel:')
  st.dataframe(df)

with col2:
  st.subheader('Linechart:')
  st.line_chart(df.set_index('Tahun'))