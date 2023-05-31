import streamlit as st
import pandas as pd
import numpy as np

# Checkbox Widget
np.random.seed(100)
df = pd.DataFrame({
  'Tahun': ['2023', '2024', '2025', '2026', '2027'],
  'Produk1': np.random.randint(100, 1000, 5),
  'Produk2': np.random.randint(100, 1000, 5),
  'Produk3': np.random.randint(100, 1000, 5)
  }, index=[1,2,3,4,5])

st.subheader('Table:')
st.dataframe(df)

show = st.checkbox('Show Linechart')
if show:
  st.markdown('#')
  st.subheader('linechart:')
  st.line_chart(df.set_index('Tahun'))