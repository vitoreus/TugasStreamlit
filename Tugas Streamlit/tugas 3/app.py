import streamlit as st
import pandas as pd
import numpy as np
import graphviz

# 1. Write and Magic
st.title("1. Write and Magic")

df = pd.DataFrame({
  'Tahun': ['2023', '2024', '2025', '2026', '2027'],
  'Produk1': np.random.randint(100, 1000, 5),
  'Produk2': np.random.randint(100, 1000, 5),
  'Produk3': np.random.randint(100, 1000, 5)
})

st.subheader("print with st.write:")
st.write(df.set_index('Tahun'))

st.write('#')
st.subheader("print with magic:")
df

# 2. Text Elements with st.code
st.write("#")
st.title("2. Text Elements")

st.markdown(":green[$c= \sqrt{a^2+b^2}$]")
code = '''
# pythagoras function
def pythagoras(a,b):
    return sqrt(a**2 + b**2);
    
result = pythagoras(3,4)
print(result)
'''
st.code(code, language='python')
st.write("result = 5")

# 3. Data Display Elements with st.checkbox and dataframe
st.write("#")
st.title("3. Data Display Elements")

df = pd.DataFrame({
  'year': ['2023', '2024', '2025', '2026', '2027'],
  'sales': [13000, 14000, 15000, 16000, 17000]
}, index=[1,2,3,4,5])

st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df.style.highlight_max(axis=0), use_container_width=st.session_state.use_container_width)

# 4. Chart Elements with st.graphviz_chart
st.write("#")
st.title("4. Chart Elements")

graph = graphviz.Digraph()
graph.edge('Mulai', 'Masukan Bilangan Bulat')
graph.edge('Masukan Bilangan Bulat', 'Bilangan di Modulus')
graph.edge('Bilangan di Modulus', 'Apakah modulus = 0')
graph.edge('Apakah modulus = 0', 'Genap')
graph.edge('Apakah modulus = 0', 'Ganjil')
graph.edge('Genap', 'Selesai')
graph.edge('Ganjil', 'Selesai')

st.graphviz_chart(graph)

#  5. Input Widgets with st.radio
st.write("#")
st.title("5. Input Widgets")

genre = st.radio(
    "2 + 2 x 2 - 2 : 2",
    ('2', '5', '6'))

if genre == '5':
    st.write('You Great')
else:
    st.write("You Wrong")

# 6. Media Elements with st.video
st.write("#")
st.title("6. Media Elements")
st.video("https://www.youtube.com/watch?v=Eh2eFk6f9zc")

# 7. Layouts and Containers with st.column
st.write("#")
st.title("7. Layouts and Containers")

col1, col2, col3 = st.columns(3)

with col1:
   st.image("https://th.bing.com/th/id/OIP.Nb4ingdcsgW_Eq2-riEDBwAAAA?pid=ImgDet&rs=1")

with col2:
   st.image("https://th.bing.com/th/id/OIP.crgFOuos0pmUeJTLROjSrQHaE6?pid=ImgDet&rs=1")

# 8. Status Elements with st.progress
st.write("#")
st.title("8. Status Elements")

if st.button('Click Button'):
    st.success('This is a success message!', icon="✅")
else:
    st.write('Please Click The Button!')

# 9. Utilities with st.echo
st.write("#")
st.title("9. Utilities with st.stop")

with st.echo():
    st.write('This code will be printed')

# 10. Control Flow with st.stop
st.write("#")
st.title("10. Control Flow")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')