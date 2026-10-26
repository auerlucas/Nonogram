# Model/Position.py
from Model.debug import *
from Model.CustomTypes import Position


#
# Les positions ne sont pas toujours faciles à gérer !
#
# Sur une image, quand on parle d'un pixel (x, y), x représente la colonne et y la ligne.
# Dans un tableau, quand on cherche la valeur tab[i][j], cette fois, c'est i qui désigne la ligne et j la colonne.
#
# Pour tenter d'éviter d'intervertir ligne/colonne, on va créer un dictionnaire avec deux clés bien explicites
# - la clé LIGNE qui représentera le numéro de ligne
# - la clé COLONNE qui représentera le numéro de colonne
#

LIGNE = "ligne"
COLONNE = "colonne"



def type_position(position: Position) -> bool:
    """
    Fonction permettant de déterminer si le paramètre peut représenter ou non une position.

    Cette fonction ne peut valider la valeur des lignes/colonnes

    :param position: Position à tester
    :return: True si le paramètre correspond à une position, False sinon
    """
    if type(position) is not dict:
        debug(f"Le paramètre {position} n'est pas un dictionnaire")
        return False
    if LIGNE not in position or COLONNE not in position:
        debug(f"Le dictionnaire {position} ne contient pas une des clés {LIGNE} ou {COLONNE}")
        return False
    if type(position[LIGNE]) is not int or type(position[COLONNE]) is not int:
        debug(f"Une des valeurs du dictionnaire {position} n'est pas un entier")
        return False
    return True


#============== DEBUT DU CODE ============================

def construirePosition()->dict[str, int]:
    """
    Initialise une position à 0 et 0 ( LIGNE = 0, COLONNE=0)
    :return: Une position
    """
    return {LIGNE:0, COLONNE:0}

def getLignePosition(pos:Position)->int:
    """
    Renvoie la valeur du numéro de la LIGNE grace au param pos
    :param pos: Une position
    :return: Entier correspondant au numéro de la LIGNE
    """
    assert type_position(pos),"param pos : mauvais type"

    return pos[LIGNE]

def getColonnePosition(pos:Position)->int:
    """
    Renvoie la valeur du numéro de la COLONNE grace au param pos
    :param pos: Une position
    :return: Entier correspondant au numéro de la COLONNE
    """
    assert type_position(pos), "param pos : mauvais type"

    return pos[COLONNE]

def setLignePosition(pos:Position, nbr:int)->None:
    """
    Attribue à la LIGNE contenu dans le param pos l'entier nbr mis en paramètre
    :param pos: Une position
    :param nbr: Un entier
    :return: Rien
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(nbr) is int, "param nbr: mauvais type"

    pos[LIGNE]=nbr

    return None

def setColonnePosition(pos:Position, nbr:int)->None:
    """
    Attribue à la COLONNE contenu dans le param pos l'entier nbr mis en paramètre
    :param pos: Une position
    :param nbr: Un entier
    :return: Rien
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(nbr) is int, "param nbr: mauvais type"

    pos[COLONNE]=nbr

    return None

def incLignePosition(pos:Position, nbr:int=1)->None:
    """
    Augmente la valeur de 1 la LIGNE contenu dans le param pos
    :param pos: Une position
    :param nbr: Un entier (par défaut : 1)
    :return: Rien
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(nbr) is int, "param nbr: mauvais type"

    #print(pos[LIGNE], end =" / ")
    pos[LIGNE]+=nbr
    #print(pos[LIGNE])

    return None

def incColonnePosition(pos:Position, nbr:int=1)->None:
    """
    Augmente la valeur de 1 la COLONNE contenu dans le param pos
    :param pos: Une position
    :param nbr: Un entier (par défaut : 1)
    :return: Rien
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(nbr) is int, "param nbr: mauvais type"

    pos[COLONNE]+=nbr

    return None

def decLignePosition(pos:Position, nbr:int=1)->None:
    """
    DIminue la valeur de 1 la LIGNE contenu dans le param pos
    :param pos: Une position
    :param nbr: Un entier (par défaut : 1)
    :return: Rien
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(nbr) is int, "param nbr: mauvais type"

    pos[LIGNE]-=nbr

    return None

def decColonnePosition(pos:Position, nbr:int=1)->None:
    """
    DIminue la valeur de 1 la COLONNE contenu dans le param pos
    :param pos: Une position
    :param nbr: Un entier (par défaut : 1)
    :return: Rien
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(nbr) is int, "param nbr: mauvais type"

    pos[COLONNE]-=nbr

    return None

