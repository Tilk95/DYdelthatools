# # coding: utf-8
#-------------------------------------------------------------------------
#   _____  _______ _____  _______ _______ _______     
#  |     \|    ___|     ||_     _|   |   |   _   |    
#  |  --  |    ___|       ||   | |       |       |    
#  |_____/|_______|_______||___| |___|___|___|___|    
#                                                     
#   _______               __                          
#  |_     _|.-----.-----.|  |.-----.                  
#    |   |  |  _  |  _  ||  ||__ --|                  
#    |___|  |_____|_____||__||_____|                 
#
#-------------------------------------------------------------------------
# DY-DELTHA-TOOLS
# date : 16/09/2023
# auteur : MBD
# updates
# 1.0 : 17/09/2023 : version initiale
# 1.1 : 18/09/2023 : Correction des empreintes
# 2.0 : 24/09/2023 : Gestion des régimes avec fourniture d'une DDA + régime Hexadécimal + régime numériques
#--------------------------------------------------------------------------

produit_name ="DELTHA TOOLS"
produit_version = "2.00"
produit_update = "24/09/2023"

import os
import sys
from datetime import datetime,timedelta


#--------------------------------------------------------------------------
# DEFINITION DES MASK 
#---------------------------------------------------------------------------

#  MASQUE PRINCIPAL ( 32 BITS ) 

dico_empreinte_principale = {
    0 : "K_PR",
    1 : "K_MARGE_REELLE",
    2 : "K_MARGE_THEORIQUE",
    3 : "K_HEURE_DEPART",
    4 : "K_HEURE_PASSAGE",
    5 : "K_HEURE_ARRIVEE",
    6 : "K_CHGT_PARITE",
    7 : "K_UI",
    8 : "K_TCT",
    9 : "K_FAMILLE",
    10 : "K_IND_COMPO",
    11 : "K_MNEMO",
    12 : "K_TONN_REF",
    13 : "K_NB_ENGIN_CALCUL",
    14 : "K_NUM_DEMANDE",
    15 : "K_NUM_DOSSIER",
    16 : "K_VOIE_ENTREE",
    17 : "K_VOIE_VIA",
    18 : "K_VOIE_SORTIE",
    19 : "K_SIGNE_CONV",
    20 : "K_FH",
    21 : "K_RENVOIS",
    22 : "K_AKM",
    23 : "K_VDS" 
}

#  MASQUE SIGNES CONVENtIONNELS ( 32 BITS ) 
dico_empreinte_signes_conv = {
    0 : "K_PL",
    1 : "K_<PL>",
    2 : "K_[PL]",
    3 : "K_D",
    4 : "K_<D>",
    5 : "K_[D]",
    6 : "K_@",
    7 : "K_[C]",
    8 : "K_S",
    9 : "K_[S]",
    10 : "K_V",
    11 : "K_X",
    12 : "K_+"
}

#  MASQUE RENVOIS 1_4 ( 32 BITS ) 
dico_empreinte_renvois_1_4 = {
	0:"K_CODE_RENV_01",
	1:"K_CODE_RENV_02",
	2:"K_CODE_RENV_03",
	3:"K_CODE_RENV_04",
	4:"K_CODE_RENV_05",
	5:"K_CODE_RENV_06",
	6:"K_CODE_RENV_07",
	7:"K_CODE_RENV_08",
	8:"K_CODE_RENV_09",
	9:"K_CODE_RENV_10",
	10:"K_CODE_RENV_11",
	11:"K_CODE_RENV_12",
	12:"K_CODE_RENV_13",
	13:"K_CODE_RENV_14",
	14:"K_CODE_RENV_15",
	15:"K_CODE_RENV_16",
	16:"K_CODE_RENV_17",
	17:"K_CODE_RENV_18",
	18:"K_CODE_RENV_19",
	19:"K_CODE_RENV_20",
	20:"K_CODE_RENV_21",
	21:"K_CODE_RENV_22",
	22:"K_CODE_RENV_23",
	23:"K_CODE_RENV_24",
	24:"K_CODE_RENV_25",
	25:"K_CODE_RENV_26",
	26:"K_CODE_RENV_27",
	27:"K_CODE_RENV_28",
	28:"K_CODE_RENV_29",
	29:"K_CODE_RENV_30",
	30:"K_CODE_RENV_31",
	31:"K_CODE_RENV_32"
}

#  MASQUE RENVOIS 2_4 ( 32 BITS ) 
dico_empreinte_renvois_2_4 = {
    0:"K_CODE_RENV_33",
    1:"K_CODE_RENV_34",
    2:"K_CODE_RENV_35",
    3:"K_CODE_RENV_36",
    4:"K_CODE_RENV_37",
    5:"K_CODE_RENV_38",
    6:"K_CODE_RENV_39",
    7:"K_CODE_RENV_40",
    8:"K_CODE_RENV_41",
    9:"K_CODE_RENV_42",
    10:"K_CODE_RENV_43",
    11:"K_CODE_RENV_44",
    12:"K_CODE_RENV_45",
    13:"K_CODE_RENV_46",
    14:"K_CODE_RENV_47",
    15:"K_CODE_RENV_48",
    16:"K_CODE_RENV_49",
    17:"K_CODE_RENV_50",
    18:"K_CODE_RENV_51",
    19:"K_CODE_RENV_52",
    20:"K_CODE_RENV_53",
    21:"K_CODE_RENV_54",
    22:"K_CODE_RENV_55",
    23:"K_CODE_RENV_56",
    24:"K_CODE_RENV_57",
    25:"K_CODE_RENV_58",
    26:"K_CODE_RENV_59",
    27:"K_CODE_RENV_60",
    28:"K_CODE_RENV_61",
    29:"K_CODE_RENV_62",
    30:"K_CODE_RENV_63",
    31:"K_CODE_RENV_64"
}


#  MASQUE RENVOIS 3_4 ( 32 BITS ) 
dico_empreinte_renvois_3_4 = {
    0:"K_CODE_RENV_65",
    1:"K_CODE_RENV_66",
    2:"K_CODE_RENV_67",
    3:"K_CODE_RENV_68",
    4:"K_CODE_RENV_69",
    5:"K_CODE_RENV_70",
    6:"K_CODE_RENV_71",
    7:"K_CODE_RENV_72",
    8:"K_CODE_RENV_73",
    9:"K_CODE_RENV_74",
    10:"K_CODE_RENV_75",
    11:"K_CODE_RENV_76",
    12:"K_CODE_RENV_77",
    13:"K_CODE_RENV_78",
    14:"K_CODE_RENV_79",
    15:"K_CODE_RENV_80",
    16:"K_CODE_RENV_81",
    17:"K_CODE_RENV_82",
    18:"K_CODE_RENV_83",
    19:"K_CODE_RENV_84",
    20:"K_CODE_RENV_85",
    21:"K_CODE_RENV_86",
    22:"K_CODE_RENV_87",
    23:"K_CODE_RENV_88",
    24:"K_CODE_RENV_89",
    25:"K_CODE_RENV_90",
    26:"K_CODE_RENV_91",
    27:"K_CODE_RENV_92",
    28:"K_CODE_RENV_93",
    29:"K_CODE_RENV_94",
    30:"K_CODE_RENV_95",
    31:"K_CODE_RENV_96"
}


#  MASQUE RENVOIS 4_4 ( 32 BITS ) 
dico_empreinte_renvois_4_4 = {
    0:"K_CODE_RENV_97",
    1:"K_CODE_RENV_98",
    2:"K_CODE_RENV_99",
    3:"K_CODE_RENV_LIBRE"
}

#----------------------------------------------------------------------------------------
# DEFINITION DES VARIABLES DIVERSES
#----------------------------------------------------------------------------------------

os_clear_command = 'cls' if sys.platform == 'win32' else 'clear' # commande pour effacer un écran en fonction du systéme.

glb_menu_titre  = ""
glb_menu_titre += "   _____  _______ _____  _______ _______ _______     \n"
glb_menu_titre += "  |     \|    ___|     ||_     _|   |   |   _   |    \n"
glb_menu_titre += "  |  --  |    ___|       ||   | |       |       |    \n"
glb_menu_titre += "  |_____/|_______|_______||___| |___|___|___|___|    \n"
glb_menu_titre += "   _______               __                          \n"
glb_menu_titre += "  |_     _|.-----.-----.|  |.-----.                  \n"
glb_menu_titre += "    |   |  |  _  |  _  ||  ||__ --|                  \n"
glb_menu_titre += "    |___|  |_____|_____||__||_____| v"+produit_version+"\n"


#-----------------------------------------------------------------------------------------------------
# Fonctions diverses
#-----------------------------------------------------------------------------------------------------
def _fct_wait(p_message):
    print(p_message)
    _st_wait = input("Appuyez sur une touche pour continuer.")

def fct_hexa_to_bin(p_hexa):
    _st_bin=""
    for _i in range(0,len(p_hexa)):
        _st_bin = _st_bin + ('0000'+(bin(int(p_hexa[_i],16))[2:]))[-4:]

    _st_bin = _st_bin.lstrip("0")

    return _st_bin



#----------------------------------------------------------------------------------------------------
#   _______     ________    ______  _____  ____    ____  ________   ______   
#  |_   __ \   |_   __  | .' ___  ||_   _||_   \  /   _||_   __  |.' ____ \  
#    | |__) |    | |_ \_|/ .'   \_|  | |    |   \/   |    | |_ \_|| (___ \_| 
#    |  __ /     |  _| _ | |   ____  | |    | |\  /| |    |  _| _  _.____`.  
#   _| |  \ \_  _| |__/ |\ `.___]  |_| |_  _| |_\/_| |_  _| |__/ || \____) | 
#  |____| |___||________| `._____.'|_____||_____||_____||________| \______.' 
#                                                                            
#----------------------------------------------------------------------------------------------------

# Affichage d'un régime Héxadécimal
#-----------------------------------------------------------------------------------------------
def fct_affiche_regime(_p_dda,_p_regime):
    #-------------------------------------------------------------------------------
    # définition des constantes 
    #-------------------------------------------------------------------------------
    Mois=['Janvier  ','Fevrier  ','Mars     ','Avril    ','Mai      ','Juin     ','Juillet  ','Aout     ','Septembre','Octobre  ','Novembre ','Decembre ']
    Jour=['L',"M","m","J","V","S","D"]

    #-------------------------------------------------------------------------------
    # Traitement des paramétres 
    #-------------------------------------------------------------------------------
    _regime = _p_regime
    _dda = datetime.strptime(_p_dda, "%Y-%m-%d")



    _dc = _dda
    _str_bin = fct_hexa_to_bin(_regime)
    _taille_regime = len(_str_bin)




    #----------------------------------------------------------------------
    # On commence par le début du régime 
    #----------------------------------------------------------------------
    _start_calendrier =""
    _int_premier_jour = _dc.day
    _start_calendrier = "   !"*(_int_premier_jour-1)

    _mois_encours = Mois[(_dc.month-1)][0:8]+" "+("0000"+str(_dc.year)[:4])[-4:]+" !"
    _ligne_calendrier = _mois_encours+_start_calendrier

    print("")
    print(" AFFICHAGE CALENDRIER ")
    print(" Date début :"+_p_dda)
    print(" Régime : "+_regime)

    print("")
    print("              -----------------------------------------------------------------------------------------------------------------------------")
    print("              !01 !02 !03 !04 !05 !06 !07 !08 !09 !10 !11 !12 !13 !14 !15 !16 !17 !18 !19 !20 !21 !22 !23 !24 !25 !26 !27 !28 !29 !30 !31 !")
    print("              -----------------------------------------------------------------------------------------------------------------------------")

    for i in range(0,_taille_regime):
        
        _str_jour_actif = " . !"
        if (_str_bin[i]=="1"):
            _str_jour_actif=" O !"
            _str_jour_actif = " "+Jour[(_dc.weekday())]+" !"
            
        if (_dc.day==1 and _dc!=_dda):
            print(_ligne_calendrier)
            _mois_encours = Mois[(_dc.month-1)][0:8]+" "+("0000"+str(_dc.year)[:4])[-4:]+" !"
            _ligne_calendrier = _mois_encours+_str_jour_actif                
        else:
            _ligne_calendrier = _ligne_calendrier+_str_jour_actif
        _dc = _dc + timedelta(days=1)

    print(_ligne_calendrier)
    print("              -----------------------------------------------------------------------------------------------------------------------------")
    print("")


def fct_lecture_regime_hexa():     
    #---------------------------------------------------------------------------------------------
    # lecture régime type HEXA
    #  Date de début du régime : AAAA-MM-JJ
    #  régime : format Héxadécimal
    #---------------------------------------------------------------------------------------------

    #---- Lecture Date début Régime : _DDR

    _error = False

    _ddr = input("Date de début du régime (format AAAA-MM-JJ) : ")
    try:
        _date_ddr = datetime.strptime(_ddr, "%Y-%m-%d")
    except:
        _fct_wait("[ERROR] format date inconnu!")
        _error = True

    #----------------------------------------------------------------------------------------------
    # lecture régime
    #-----------------------------------------------------------------------------------------------
    if (not _error):
        _regime = input("Régime Héxadécimal : ")
        try:
            _str_bin = bin(int(_regime,16))[2:]
        except:
            _fct_wait("[ERROR] format de régime inconnu!")
            _error = True
            

    #----------------------------------------------------------------------------------------------
    # _DDR et régime correct
    #-----------------------------------------------------------------------------------------------
    if (not _error):
        fct_affiche_regime(_ddr,_regime)
        mon_wait = input("APPUYER SUR ENTREE POUR CONTINUER")


def fct_lecture_regime_numerique():     
    #---------------------------------------------------------------------------------------------
    # lecture régime type numériques ( 6 numériques )
    #  Date de début du régime : AAAA-MM-JJ
    #  régimes : format integer
    #---------------------------------------------------------------------------------------------

    #---- Lecture Date début Régime : _DDR

    _st_regime ="" 
    
    _error = False

    _ddr = input("Date de début DE SERVICE (format AAAA-MM-JJ) : ")
    try:
        _date_ddr = datetime.strptime(_ddr, "%Y-%m-%d")
    except:
        _fct_wait("[ERROR] format date inconnu!")
        _error = True

    #----------------------------------------------------------------------------------------------
    # lecture régime numérique 
    #-----------------------------------------------------------------------------------------------
    if (not _error):
        _tab_regime=['','','','','','']
        
        for _idx in range(0,6):
            _str_regime = input("Régime Part "+str(_idx+1)+" : ")
            try:
                _int_regime = int(_str_regime)
            except:
                _fct_wait("[ERROR] format inconnu!")
                _error = True
            if (not _error):
                if (_int_regime<0 or _int_regime>(2**64)-1):
                    _fct_wait("[ERROR] le régime doit être >=0 et <="+str((2**64)-1)+"!")
                    _error = True
                else:
                    _tab_regime[_idx] = (('00'*8+hex(_int_regime).lstrip('0x').upper())[-16:])
            if (_error): break
        
        if(not _error):
            fct_affiche_regime(_ddr,_st_regime)
            mon_wait = input("APPUYER SUR ENTREE POUR CONTINUER")

#----------------------------------------------------------------------------------------------------
#   ________  ____    ____  _______  _______     ________  _____  ____  _____  _________  ________   ______   
#  |_   __  ||_   \  /   _||_   __ \|_   __ \   |_   __  ||_   _||_   \|_   _||  _   _  ||_   __  |.' ____ \  
#    | |_ \_|  |   \/   |    | |__) | | |__) |    | |_ \_|  | |    |   \ | |  |_/ | | \_|  | |_ \_|| (___ \_| 
#    |  _| _   | |\  /| |    |  ___/  |  __ /     |  _| _   | |    | |\ \| |      | |      |  _| _  _.____`.  
#   _| |__/ | _| |_\/_| |_  _| |_    _| |  \ \_  _| |__/ | _| |_  _| |_\   |_    _| |_    _| |__/ || \____) | 
#  |________||_____||_____||_____|  |____| |___||________||_____||_____|\____|  |_____|  |________| \______.' 
# 
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#- afficher dictionnaire 
#-  input : p_dico : le dictionnaire � afficher 
#----------------------------------------------------------------------------------------
def fct_liste_dico(p_dico):
    print("Description de l'empreinte\n")
    print("\tBIT\tCodes\t")
    for i, (idx,key) in enumerate(p_dico.items()):
        print("\t",idx,"\t ",key)
        
#----------------------------------------------------------------------------------------
def fct_get_liste_dico(p_dico):
    _text = ""
    for i, (idx,key) in enumerate(p_dico.items()):
        _text += key+";"        
    return _text

#----------------------------------------------------------------------------------------
#- concertir un mask en texte  
#-  input : p_mask : le mask  à afficher 
#-----------------------------------------------
def fct_mask_to_txt(p_mask:int,p_dico):
    _str_return = ""
    _str_bin = bin(p_mask)[2:]
#    _str_bin= _str_bin[::-1]+"".zfill(32)
    _str_bin= "".zfill(32)+_str_bin
    _str_bin=_str_bin[-32:]
    for i in range(0,len(_str_bin)): 
        _str_bit = _str_bin[i:(i+1)]
        _search = i
        if (_str_bit=="1") :
            for j, (idx,key) in enumerate(p_dico.items()):
                if (_search == idx):
                    _str_return += key +";"
                    break

    return _str_return

#----------------------------------------------------------------------------------------
#- convertir un texte en mask ( numérique )  
#-  input : p_text : le texte avec des séparateurs, exemples : 
#-              p_text : K_UI+K_TCT+K_VOIE_ENTREE
#-----------------------------------------------
def fct_txt_to_mask(p_text:str,p_dico):
    _tab_parametres = p_text.strip().upper().split("+")
    _int_mask = 0

    for parametre in _tab_parametres:
        for j, (idx,key) in enumerate(p_dico.items()):
            if (parametre == key):
                if (idx>=0 and idx<=31):
                    _int_mask = _int_mask|(2**(31-idx))
                    break
    return _int_mask

#----------------------------------------------------------------------------------------
#- convertir un texte en mask ( numérique )  
#-  input : p_text : le texte avec des séparateurs, exemples : 
#-              p_text : K_UI;K_TCT;K_VOIE_ENTREE
#-----------------------------------------------
def fct_mask_to_bin(p_mask:int):
    _str_bin = bin(p_mask)[2:]           
    return _str_bin

def fct_print_resultat(p_mask_int,p_dico,p_lib_dico=""):
    p_mask_text = fct_mask_to_txt(p_mask_int,p_dico)
    p_mask_binaire = 0
    p_mask_binaire = bin(p_mask_int)[2:]
    p_mask_binaire = "".zfill(32)+p_mask_binaire
    p_mask_binaire = p_mask_binaire[-32:]

    print("\n---------------------------------------------------------------------------")
    print(f" - MASK NUMERIQUE : {p_mask_int}")
    print(f" - Masque Binaire : {p_mask_binaire}")
    _cpt = 0
    _texte = ""
    _tab_p_mask_text = p_mask_text.split(";")

    print(f" - CONTENU ( TEXTE ) : ")
    for _text in _tab_p_mask_text:
        if _text.strip()!='' : print("\t\t\t"+_text)
    print("---------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------
def fct_empreinte_description(p_dico):
    print("\n")
    _txt = fct_liste_dico(p_dico)
    print("\n")
    mon_wait = input("APPUYER SUR ENTREE POUR CONTINUER")
    
#--------------------------------------------------------------------------------------
# Lecture d'un mask au format NUMERIQUE
#--------------------------------------------------------------------------------------

def fct_empreinte_lire_numerique(p_dico):
    _int_taille_dico = 0
    _int_taille_dico = 32
    _int_max = 2**_int_taille_dico -1
         
    print("\n")

    mon_numerique = input("SAISIR L'EMPREINTE NUMERIQUE (max "+str(_int_max)+"): ")
    try:
        int_numerique = int(mon_numerique)
        if (int_numerique<=_int_max):
            fct_print_resultat(int_numerique,p_dico)
        else:
            print("La valeur saisie ne peut dépasser : "+str(_int_max)+"\n")
    except ValueError:
        print("ERREUR : format inconnu!\n")

    print("\n")
    mon_wait = input("APPUYER SUR ENTREE POUR CONTINUER")
    
#--------------------------------------------------------------------------------------
# Lecture d'un mask au format BINAIRE
#--------------------------------------------------------------------------------------

def fct_empreinte_lire_binaire(p_dico):
    
    _int_taille_dico = 0
    _int_taille_dico = len(p_dico)
    _int_taille_dico = 32
    
    print("\n")

    mon_numerique = input("SAISIR L'EMPREINTE BINAIRE ( max "+str(_int_taille_dico)+" bits ): ")
    if (mon_numerique.strip()!='' and mon_numerique!=None and mon_numerique>="0" and mon_numerique<="9"):
        try:
            ma_chaine = mon_numerique+"".zfill(32)
            ma_chaine = ma_chaine[0:32]
            int_numerique = int(ma_chaine,2)
            int_binaire = ma_chaine
            
            if (len(mon_numerique)<=_int_taille_dico):
                fct_print_resultat(int_numerique,p_dico)
            else:
                print("ERREUR : chaine binaire trop longue ( "+str(len(mon_numerique))+">"+str(_int_taille_dico)+" ) !\n")
        except ValueError:
            print("ERREUR : chaine binaire inconnue!\n")

    print("\n")

    mon_wait = input("APPUYER SUR ENTREE POUR CONTINUER")

#--------------------------------------------------------------------------------------
# Lecture d'un mask sous format TEXTE en suivant le format :
# K_PR+K_UI+K_TCT
#---------------------------------------------------------------------------------------
def fct_empreinte_lire_texte(p_dico):
    print("\n")

    print("Pour saisir l'EMPREINTE TEXTE, utiliser les codes ci-dessous separes par des '+' \n")
    fct_liste_dico(p_dico)
    print("\n")
    
    mon_texte = input("SAISIR L'EMPREINTE TEXTE : ")
    if (mon_texte.strip()!='' and mon_texte!=None):
        _text = mon_texte.strip()
        int_numerique = fct_txt_to_mask(_text,p_dico)
        fct_print_resultat(int_numerique,p_dico)

    print("\n")

    mon_wait = input("APPUYER SUR ENTREE POUR CONTINUER")
    

#----------------------------------------------------------------------------------------------
#   ____    ____  ________  ____  _____  _____  _____   ______   
#  |_   \  /   _||_   __  ||_   \|_   _||_   _||_   _|.' ____ \  
#    |   \/   |    | |_ \_|  |   \ | |    | |    | |  | (___ \_| 
#    | |\  /| |    |  _| _   | |\ \| |    | '    ' |   _.____`.  
#   _| |_\/_| |_  _| |__/ | _| |_\   |_    \ \__/ /   | \____) | 
#  |_____||_____||________||_____|\____|    `.__.'     \______.' 
#       
#----------------------------------------------------------------------------------------------
    
#----------------------------------------------------------------------------------------------
# MENU "EMPREINTES" 
#----------------------------------------------------------------------------------------------

def fct_menu_empreintes(p_dico,p_lib):
    
    _int_taille_dico = 0
    _int_taille_dico = len(p_dico)
    
    
    glb_menu_empreinte = ""
    glb_menu_empreinte += " MENU "+p_lib+" ( max "+str(_int_taille_dico)+" bits ) \n"
    glb_menu_empreinte += "\n"
    glb_menu_empreinte += "     01 - LIRE EMPREINTE NUMERIQUE \n"
    glb_menu_empreinte += "     02 - LIRE EMPREINTE BINAIRE \n"
    glb_menu_empreinte += "     03 - LIRE EMPREINTE TEXTE \n"
    glb_menu_empreinte += "     04 - DESCRIPTION EMPREINTE \n"
    glb_menu_empreinte += "\n"
    glb_menu_empreinte += " 99 - RETOUR MENU PRINCIPAL \n"
    glb_menu_empreinte += "\n"
    
    while (1==1):
        os.system(os_clear_command)
        print(glb_menu_titre)
        print(glb_menu_empreinte)
        int_rep = 0
        ma_reponse = input("VOTRE CHOIX :")  
        try:
            int_rep = int(ma_reponse)
            pass
        except ValueError:
            pass
        
        # utilisation des IF et pas Match pour compatibilité avec les vielles versions de Python
        if int_rep==99 : break
        if int_rep== 1 : fct_empreinte_lire_numerique(p_dico)
        if int_rep==2 : fct_empreinte_lire_binaire(p_dico)
        if int_rep==3 : fct_empreinte_lire_texte(p_dico)
        if int_rep==4 : fct_empreinte_description(p_dico)           
    pass

#----------------------------------------------------------------------------------------------
# MENU "REGIMES" 
#----------------------------------------------------------------------------------------------

def fct_menu_regimes():
    
    
    glb_menu_empreinte = ""
    glb_menu_empreinte += " MENU GESTION DES REGIMES \n"
    glb_menu_empreinte += "\n"
    glb_menu_empreinte += "     01 - INTERPRETER UN REGIME HEXA \n"
    glb_menu_empreinte += "     02 - INTERPRETER UN REGIME NUMERIQUE \n"
    glb_menu_empreinte += "\n"
    glb_menu_empreinte += " 99 - RETOUR MENU PRINCIPAL \n"
    glb_menu_empreinte += "\n"
    
    while (1==1):
        os.system(os_clear_command)
        print(glb_menu_titre)
        print(glb_menu_empreinte)
        int_rep = 0
        ma_reponse = input("VOTRE CHOIX :")  
        try:
            int_rep = int(ma_reponse)
            pass
        except ValueError:
            pass
        
        # utilisation des IF et pas Match pour compatibilité avec les vielles versions de Python
        if int_rep==99 : break
        if int_rep== 1 : fct_lecture_regime_hexa()
        if int_rep== 2 : fct_lecture_regime_numerique()
    pass


if __name__ == "__main__":
    #----------------------------------------------------------------------------------------------
    #- Main menu
    #----------------------------------------------------------------------------------------------

    glb_menu_main_menu = ""
    glb_menu_main_menu += " MENU PRINCIPAL\n"
    glb_menu_main_menu += "\n"
    glb_menu_main_menu += "     01 - EMPREINTE PRINCIPALE \n"
    glb_menu_main_menu += "\n"
    glb_menu_main_menu += "     02 - EMPREINTE SIGNES CONVENTIONNELS \n"
    glb_menu_main_menu += "\n"
    glb_menu_main_menu += "     21 - EMPREINTES RENVOIS 01..32\n"
    glb_menu_main_menu += "     22 - EMPREINTES RENVOIS 33..64\n"
    glb_menu_main_menu += "     23 - EMPREINTES RENVOIS 64..96\n"
    glb_menu_main_menu += "     24 - EMPREINTES RENVOIS 96..99 + LIBRE \n"
    glb_menu_main_menu += "\n"
    glb_menu_main_menu += "     31 - GESTION DES REGIMES \n"

    glb_menu_main_menu += "\n"
    glb_menu_main_menu += " 99 - QUITTER \n"
    glb_menu_main_menu += "\n"

    while (1==1):
        os.system(os_clear_command)
        print(glb_menu_titre)
        print(glb_menu_main_menu)
        ma_reponse = input("VOTRE CHOIX :")
        int_rep = 0
        try :
            int_rep = int(ma_reponse)
            pass
        except ValueError:
            pass

        if int_rep== 99 : break
        if int_rep==1 : fct_menu_empreintes(dico_empreinte_principale,"EMPREINTE PRINCIPALE")
        if int_rep==2 : fct_menu_empreintes(dico_empreinte_signes_conv,"EMPREINTE SIGNES CONV.")

        if int_rep==21 : fct_menu_empreintes(dico_empreinte_renvois_1_4,"EMPREINTE RENVOIS 01..32")
        if int_rep==22 : fct_menu_empreintes(dico_empreinte_renvois_2_4,"EMPREINTE RENVOIS 32..64")
        if int_rep==23 : fct_menu_empreintes(dico_empreinte_renvois_3_4,"EMPREINTE RENVOIS 64..96")
        if int_rep==24 : fct_menu_empreintes(dico_empreinte_renvois_4_4,"EMPREINTE RENVOIS 96..99 + LIBRE ")

        if int_rep==31 : fct_menu_regimes()




