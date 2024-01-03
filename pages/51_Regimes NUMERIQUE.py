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
def fct_lire_numeriques():
    _return = ""
#    _int_max = 2**64
    _int_max = 18446744073709551615

    _tab_regime = ['', '', '', '', '', '']

    col1,col2,col3 = st.columns(3)

    # Regime 1
    _int_regime_1 = 0
    _str_regime_1 = col1.text_input('Régime Part 1 ')
    _str_regime_1 = _str_regime_1.strip()
    try:
        _int_regime_1 = int(_str_regime_1)
        if (_str_regime_1!=''):
            if (_int_regime_1<0 or _int_regime_1>_int_max):
                col1.write("[ERROR] Le régime doit être > 0 et <= "+str(_int_max))
            else:
                col1.write(('00' * 8 + hex(_int_regime_1).lstrip('0x').upper())[-16:])
    except:
        if _str_regime_1 !='':
            col1.write("[ERROR] Format inconnu ")
        _int_regime_1 = 0

    # Regime 2
    _int_regime_2 = 0
    _str_regime_2 = col2.text_input('Régime Part 2 ')
    _str_regime_2 = _str_regime_2.strip()
    try:
        _int_regime_2 = int(_str_regime_2)
        if (_str_regime_2!=''):
            if (_int_regime_2<0 or _int_regime_2>_int_max):
                col2.write("[ERROR] Le régime doit être > 0 et <= "+str(_int_max))
            else:
                col2.write(('00' * 8 + hex(_int_regime_2).lstrip('0x').upper())[-16:])
    except:
        if _str_regime_2 !='':
            col2.write("[ERROR] Format inconnu ")
        _int_regime_2 = 0


    # Regime 3
    _int_regime_3 = 0
    _str_regime_3 = col3.text_input('Régime Part 3 ')
    _str_regime_3 = _str_regime_3.strip()
    try:
        _int_regime_3 = int(_str_regime_3)
        if (_str_regime_3!=''):
            if (_int_regime_3<0 or _int_regime_3>_int_max):
                col3.write("[ERROR] Le régime doit être > 0 et <= "+str(_int_max))
            else:
                col3.write(('00' * 8 + hex(_int_regime_3).lstrip('0x').upper())[-16:])
    except:
        if _str_regime_3 !='':
            col3.write("[ERROR] Format inconnu ")
        _int_regime_3 = 0

    # Regime 4
    _int_regime_4 = 0
    _str_regime_4 = col1.text_input('Régime Part 4 ')
    _str_regime_4 = _str_regime_4.strip()
    try:
        _int_regime_4 = int(_str_regime_4)
        if (_str_regime_4!=''):
            if (_int_regime_4<0 or _int_regime_4>_int_max):
                col1.write("[ERROR] Le régime doit être > 0 et <= "+str(_int_max))
            else:
                col1.write(('00' * 8 + hex(_int_regime_4).lstrip('0x').upper())[-16:])
    except:
        if _str_regime_4 !='':
            col1.write("[ERROR] Format inconnu ")
        _int_regime_4 = 0


    # Regime 5
    _int_regime_5 = 0
    _str_regime_5 = col2.text_input('Régime Part 5 ')
    _str_regime_5 = _str_regime_5.strip()
    try:
        _int_regime_5 = int(_str_regime_5)
        if (_str_regime_5!=''):
            if (_int_regime_5<0 or _int_regime_5>_int_max):
                col2.write("[ERROR] Le régime doit être > 0 et <= "+str(_int_max))
            else:
                col2.write(('00' * 8 + hex(_int_regime_5).lstrip('0x').upper())[-16:])
    except:
        if _str_regime_5 !='':
            col2.write("[ERROR] Format inconnu ")
        _int_regime_5 = 0


    # Regime 6
    _int_regime_6 = 0
    _str_regime_6 = col3.text_input('Régime Part 6 ')
    _str_regime_6 = _str_regime_6.strip()
    try:
        _int_regime_6 = int(_str_regime_6)
        if (_str_regime_6!=''):
            if (_int_regime_6<0 or _int_regime_6>_int_max):
                col3.write("[ERROR] Le régime doit être > 0 et <= "+str(_int_max))
            else:
                col3.write(('00' * 8 + hex(_int_regime_6).lstrip('0x').upper())[-16:])
    except:
        if _str_regime_6 !='':
            col3.write("[ERROR] Format inconnu ")
        _int_regime_6 = 0

    _st_regime = ''
    _st_regime = _st_regime + (('00' * 8 + hex(_int_regime_1).lstrip('0x').upper())[-16:])
    _st_regime = _st_regime + (('00' * 8 + hex(_int_regime_2).lstrip('0x').upper())[-16:])
    _st_regime = _st_regime + (('00' * 8 + hex(_int_regime_3).lstrip('0x').upper())[-16:])
    _st_regime = _st_regime + (('00' * 8 + hex(_int_regime_4).lstrip('0x').upper())[-16:])
    _st_regime = _st_regime + (('00' * 8 + hex(_int_regime_5).lstrip('0x').upper())[-16:])
    _st_regime = _st_regime + (('00' * 8 + hex(_int_regime_6).lstrip('0x').upper())[-16:])

    if _st_regime!='00'*8*6:
        st.write("---------------------------------------------------------------------------")

        _c1 = '0DB7CB'
        _c2 = '190DCB'

        st.write("#### Régime HEXA")
        _joli_regime  =f'<span style="color:#{_c1}">{_st_regime[0:16].lstrip("0")}</span>'
        _joli_regime +=f'<span style="color:#{_c2}">{_st_regime[16:32]}</span>'

        _joli_regime +=f'<span style="color:#{_c1}">{_st_regime[32:48]}</span>'
        _joli_regime +=f'<span style="color:#{_c2}">{_st_regime[48:64]}</span>'

        _joli_regime +=f'<span style="color:#{_c1}">{_st_regime[64:80]}</span>'
        _joli_regime +=f'<span style="color:#{_c2}">{_st_regime[80:96]}</span>'

        st.markdown(_joli_regime,unsafe_allow_html=True)
        st.write("---------------------------------------------------------------------------")

        #        st.code(_st_regime)

#        st.write(_st_regime)
        _return = _st_regime

    else:
        _return =''

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
    st.write(f"### AFFICHAGE CALENDRIER {_str_bin.count('1')} jour(s) actif(s)")

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


st.write("## Consultation des REGIMES 'NUMERIQUE'")
_DDR = st.date_input("Date du début de régime ",format="DD/MM/YYYY")

_hexa = fct_lire_numeriques()

if _hexa!="":
    fct_affiche_regime(_DDR,_hexa)

    pass
