import streamlit as st
import dytools as dyt

st.set_page_config(
    page_title="Empreintes",
    page_icon="👋",
)

k_description = "Interpréteur d'Empreinte Renvois 01-32"
k_dico = dyt.dico_empreinte_renvois_1_4

st.write(f"## {k_description}")

r_type = st.radio("Vous désirez lire une empreinte ",["NUMERIQUE", "BINAIRE", "TEXTE"],horizontal=True)

def fct_lire_numerique():
    _int_taille_dico = 0
    _int_taille_dico = 32
    _int_max = 2**_int_taille_dico -1

    number = st.number_input('SAISIR L\'EMPREINTE NUMERIQUE ',min_value=0,max_value=_int_max,format="%i")
    _return = number
    return _return


def fct_lire_binaire():
    _int_taille_dico = 0
    _int_taille_dico = 32

    _return = 0

    mon_numerique = st.text_input ("SAISIR L'EMPREINTE BINAIRE ( max " + str(_int_taille_dico) + " bits ): ",max_chars=_int_taille_dico)

    if (mon_numerique.strip() != '' and mon_numerique != None and mon_numerique >= "0" and mon_numerique <= "9"):
        try:
            ma_chaine = mon_numerique + "".zfill(32)
            ma_chaine = ma_chaine[0:32]
            int_numerique = int(ma_chaine, 2)
            _return = int_numerique

        except ValueError:
            st.write("ERREUR : chaine binaire inconnue!\n")

    return _return


def fct_lire_texte(p_dico):
    print("\n")
    _return = 0
    st.write("Pour saisir l'EMPREINTE TEXTE, utiliser les codes ci-dessous separes par des '+' \n")
    st.write("Exemple : K_FH+K_TCT+K_UI \n")


    mon_texte = st.text_input("SAISIR L'EMPREINTE TEXTE : ")
    if (mon_texte.strip() != '' and mon_texte != None):
        _text = mon_texte.strip()
        int_numerique = dyt.fct_txt_to_mask(_text, p_dico)
        _return = int_numerique

    return _return


def fct_print_resultat(p_mask_int, p_dico, p_view_dico=True,p_lib_dico=""):
    p_mask_text = dyt.fct_mask_to_txt(p_mask_int, p_dico)
    p_mask_binaire = 0
    p_mask_binaire = bin(p_mask_int)[2:]
    p_mask_binaire = "".zfill(32) + p_mask_binaire
    p_mask_binaire = p_mask_binaire[-32:]


    st.write("\n---------------------------------------------------------------------------")
    st.subheader("Résultat de l'interrogation")
    st.write(f" - MASK NUMERIQUE : {p_mask_int}")
    st.write(f" - Masque Binaire : {p_mask_binaire}")
    _cpt = 0
    _texte = ""
    _tab_p_mask_text = p_mask_text.split(";")

    st.write(f" - CONTENU ( TEXTE ) : ")
    st.write(_tab_p_mask_text)
    st.write("---------------------------------------------------------------------------")
    if p_view_dico:
        st.subheader("Description de l'empreinte")
        st.write(p_dico)

if r_type=="NUMERIQUE":
    _numerique = 0
    _numerique = fct_lire_numerique()
    fct_print_resultat(_numerique,k_dico)

if r_type=="BINAIRE":
    _numerique = 0
    _numerique = fct_lire_binaire()
    fct_print_resultat(_numerique,k_dico)

if r_type=="TEXTE":
    st.write("Pour composer l'EMPREINTE TEXTE, cochez les codes ci-dessous \n")

    _numerique = 0
    _col1,_col2,_col3= st.columns(3)
    _idx_cols = 1
    t = []
    for _idx in range(len(k_dico)):
        _key = 'EMPREINTE_'+str(_idx)
        if _idx_cols == 1:
            t.append(_col1.toggle(k_dico[_idx],key=_key))
            _idx_cols = 2
        elif _idx_cols == 2:
            t.append(_col2.toggle(k_dico[_idx],key=_key))
            _idx_cols = 3
        elif _idx_cols == 3:
            t.append(_col3.toggle(k_dico[_idx],key=_key))
            _idx_cols = 1

    _numerique = 0

    for _idx in range(len(t)):
        if t[_idx]:
            _numerique = _numerique+2**(31-_idx)

    fct_print_resultat(_numerique,k_dico,False)
