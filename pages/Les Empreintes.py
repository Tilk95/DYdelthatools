import streamlit as st
import dytools as dyt

st.set_page_config(
    page_title="Empreintes",
    page_icon="👋", 
)

st.write("## Consultation des Empreintes BINAIRES!")

col1,col2 = st.columns(2)

col1.subheader("Empreintes Principales")
col1.write(dyt.dico_empreinte_principale)

col2.subheader("Empreintes SC")
col2.write(dyt.dico_empreinte_signes_conv)

st.subheader("Empreintes RENVOIS")
col1_empreinte_renvois,col2_empreinte_renvois = st.columns(2)

col1_empreinte_renvois.subheader("Renvois 1")
col1_empreinte_renvois.write(dyt.dico_empreinte_renvois_1_4)

col2_empreinte_renvois.subheader("Renvois 2")
col2_empreinte_renvois.write(dyt.dico_empreinte_renvois_2_4)


col1_empreinte_renvois,col2_empreinte_renvois = st.columns(2)

col1_empreinte_renvois.subheader("Renvois 3")
col1_empreinte_renvois.write(dyt.dico_empreinte_renvois_3_4)

col2_empreinte_renvois.subheader("Renvois 4")
col2_empreinte_renvois.write(dyt.dico_empreinte_renvois_4_4)
