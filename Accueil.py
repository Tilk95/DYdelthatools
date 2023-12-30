import streamlit as st
import dytools as dyt

st.set_page_config(
    page_title="Acceuil",
    page_icon="👋",
)

st.write("# DELTHA TOOLS 👋")

st.text(dyt.glb_menu_titre)

st.write("Outil d'aide à la compréhension des concepts Deltha.")

