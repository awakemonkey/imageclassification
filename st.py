import streamlit as st
import streamlit.components.v1 as cp



st.write("""
## Image Classification Prototype
""")


st.write("""
#### Peng Kong
""")

cp.html("<br>,<br>")

st.sidebar.info("This prototype  wiritten to help you understand how the trained Image Classification model help cusotmer to identify loosen items when self-checking in supermarket.")
dataset_name = st.sidebar.selectbox("Select Item to identify", ("None", "Apple", "Banana", "Eggplant"))
st.sidebar.write("Item you select to identify:")
st.sidebar.write(dataset_name)