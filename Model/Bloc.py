# Model/Bloc.py
#

from Model.CustomTypes import Bloc

# Clé pour stocker le nombre de cellules contigües de même couleur (bloc)
NOMBRE = "nombre"
# Couleur des cellules contigües du bloc
COULEUR = "couleur"
# Booléen permettant de savoir si l'utilisateur a découvert ou non le bloc correspondant
VU = "vu"


def type_bloc(bloc: Bloc) -> bool:
    """
    Détermine si le paramètre peut correspondre ou non à un bloc.

    Un bloc est un dictionnaire contenant 3 clés (NOMBRE, COULEUR, VU) auquelles
    sont associées des valeurs de type (int, int, bool).

    :param bloc: Objet à tester
    :return: True si l'objet correspond à un bloc, False sinon.
    """
    if type(bloc) is not dict:
        return False
    if len(bloc) != 3 or NOMBRE not in bloc or COULEUR not in bloc or VU not in bloc:
        return False
    if type(bloc[NOMBRE]) is not int or bloc[NOMBRE]<=0:
        return False
    if type(bloc[COULEUR]) is not int or bloc[COULEUR]<=0:
        return False
    if type(bloc[VU]) is not bool:
        return False
    return True

def construireBloc(nbrCellules:int,nbrCouleur:int)->Bloc:
    """
    Construction d'un bloc contenant un nombre nbrCellules de cellules et de couleur nbrCouleur
    :param nbrCellules: nombre de cellules
    :param nbrCouleur: nombre de la couleur
    :return: renvoie un bloc
    """
    assert type(nbrCellules) is int, "param nbrCellules : mauvais type"
    assert type(nbrCouleur) is int, "param nbrCouleur : mauvais type"
    assert nbrCellules>0,"param nbrCellules : le nombre de cellules saisit est plus petit que 0"
    assert nbrCouleur>0,"param nbrCouleur : le nombre de la couleur choisi est plus petit que 0"

    bloc={
        NOMBRE:nbrCellules,
        COULEUR:nbrCouleur,
        VU:False
    }
    return bloc

def getNombreBloc(bloc:Bloc)->int:
    """
    DOnne la valeur de NOMBRE (de cellules) du bloc bloc
    :param bloc: Un bloc
    :return: retourne le nombre de cellules
    """
    assert type_bloc(bloc),("param bloc : mauvais type")

    return bloc[NOMBRE]

def getCouleurBloc(bloc:Bloc)->int:
    """
    DOnne la valeur de COULEUR du bloc bloc
    :param bloc: Un bloc
    :return: retourne le nombre de la couleur
    """
    assert type_bloc(bloc),("param bloc : mauvais type")

    return bloc[COULEUR]

def isVuBloc(bloc:Bloc)->bool:
    """
    Donne la valeur de VU du bloc
    :param bloc: un bloc
    :return: retourne True si le bloc est vu, faux sinon
    """
    assert type_bloc(bloc),("param bloc : mauvais type")

    return bloc[VU]

def setVuBloc(bloc:Bloc,vu:bool)->None:
    """
    Change la valeur de VU du bloc bloc par le booleen vu
    :param bloc: un bloc
    :param vu: true or false
    :return: Rien
    """
    assert type_bloc(bloc),"param bloc : mauvais type"
    assert type(vu) is bool, "param vu : mauvais type"

    bloc[VU]=vu

    return None
