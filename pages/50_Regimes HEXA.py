import streamlit as st
import dytools as dyt
from datetime import datetime,timedelta



st.set_page_config(
    page_title="REGIME",
    page_icon="👋",
    layout="wide"
)

def fct_lire_hexa():
    _return = ""
    _regime = st.text_input("REGIME HEXADECIMAL")
    try:
        _str_hexa = bin(int(_regime,16))[2:]
        _return = _regime
    except:
        if _regime!='':
            st.write("[ERROR] Format héxadécimal incorrect")

        _return = ""

    return _return


def fct_affiche_regime(_p_dda, _p_regime):
    # -------------------------------------------------------------------------------
    # définition des constantes
    # -------------------------------------------------------------------------------
    Mois = ['Jan.', 'Fév.', 'Mars', 'Avr.', 'Mai ', 'Juin', 'Juil', 'Aout',
            'Sep.', 'Oct.', 'Nov.', 'Dec.']
    Jour = ['L', "M", "m", "J", "V", "S", "D"]

    # -------------------------------------------------------------------------------
    # Traitement des paramétres
    # -------------------------------------------------------------------------------
    _regime = _p_regime
    # _dda = datetime.strptime(_p_dda, "%Y-%m-%d")
    _dda = _p_dda


    _dc = _dda
    _str_bin = dyt.fct_hexa_to_bin(_regime)
    _taille_regime = len(_str_bin)

    # ----------------------------------------------------------------------
    # On commence par le début du régime
    # ----------------------------------------------------------------------
    _start_calendrier = ""
    _int_premier_jour = _dc.day
    _start_calendrier = "   !" * (_int_premier_jour - 1)

    _mois_encours = Mois[(_dc.month - 1)][0:4] + " " + ("0000" + str(_dc.year)[:4])[-2:] + "!"
    _ligne_calendrier = _mois_encours + _start_calendrier

    st.write("")
    st.write("### AFFICHAGE CALENDRIER ")

    _ligne_out  = "       -----------------------------------------------------------------------------------------------------------------------------\n"
    _ligne_out += "       !01 !02 !03 !04 !05 !06 !07 !08 !09 !10 !11 !12 !13 !14 !15 !16 !17 !18 !19 !20 !21 !22 !23 !24 !25 !26 !27 !28 !29 !30 !31 !\n"
    _ligne_out += "       -----------------------------------------------------------------------------------------------------------------------------\n"

    for i in range(0, _taille_regime):

        _str_jour_actif = " . !"
        if (_str_bin[i] == "1"):
            _str_jour_actif = " O !"
            _str_jour_actif = " " + Jour[(_dc.weekday())] + " !"

        if (_dc.day == 1 and _dc != _dda):
            _ligne_out += _ligne_calendrier+"\n"
            _mois_encours = Mois[(_dc.month - 1)][0:4] + " " + ("0000" + str(_dc.year)[:4])[-2:] + "!"
            _ligne_calendrier = _mois_encours + _str_jour_actif
        else:
            _ligne_calendrier = _ligne_calendrier + _str_jour_actif
        _dc = _dc + timedelta(days=1)

    _ligne_out += _ligne_calendrier + "\n"
    _ligne_out += "       -----------------------------------------------------------------------------------------------------------------------------"+"\n"
    _ligne_out +=""+"\n"

    _ligne_out = _ligne_out.replace("\n", "<br>")
    _ligne_out = _ligne_out.replace(" ", "&nbsp;")
    _ligne_out = _ligne_out.replace("!","|")

    st.markdown(f'<h1 style="color:#606060;font-size:15px;font-family:Courier New;line-height:16px;letter-spacing:-2px;margin:0px">{_ligne_out}</h1>',
                unsafe_allow_html=True)


st.write("## Consultation des REGIMES 'HEXA'")
_DDR = st.date_input("Date du début de régime ",format="DD/MM/YYYY")

_hexa = "0"
_hexa = fct_lire_hexa()
st.write("---------------------------------------------------------------------------")

if _hexa!="":
    fct_affiche_regime(_DDR,_hexa)

    pass
