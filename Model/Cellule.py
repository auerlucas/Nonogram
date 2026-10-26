# Model/Cellule.py
#

from Model.debug import debug
from Model.CustomTypes import Cellule

# Clé contenant la valeur d'une cellule
VALEUR = "value"

#
# La Cellule
#
# L'objet cellule va représenter une case de l'image (du nonogram)
#
# La cellule sera représentée par un dictionnaire.
# Une cellule pourra être :
#   - vide (absence de bille) : La valeur sera 0.
#   - non découverte (non connue) : la valeur sera None.
#   - une couleur (ou plutôt l'indice non nul d'une couleur, la palette sera fournie plus tard).
#



def type_cellule(cell: Cellule) -> bool:
    """
    Permet de vérifier si l'argument peut correspondre ou non à une cellule

    :param cell: Objet dont on veut tester le type
    :return: True s'il s'agit d'une cellule, False sinon.
    """
    if type(cell) is not dict:
        debug(f"La cellule {cell} n'est pas un dictionnaire")
        return False
    if VALEUR not in cell:
        debug(f"La clé VALUE ({VALEUR}) n'est pas dans le dictionnaire")
        return False
    if cell[VALEUR] is not None and type(cell[VALEUR]) is not int:
        debug(f"La valeur {cell[VALEUR]} n'est ni entière ni None ")
        return False
    return True


#=============== DEBUT DU CODE ===================================

def construireCellule()->Cellule:
    """
    Construit une cellule vide
    :return:Un dictionnaire contenant l’unique clé VALEUR dont la valeur associée vaudra None.
    """
    return {VALEUR:None}

def isVuCellule(cell:Cellule)->bool:
    """
    Regarde si une cellule est découverte ou non
    :param cel: Une cellule (vide ou non)
    :return: Vrai si la cellule est découverte, faux sinon
    """
    assert type_cellule(cell), "param cell : mauvais type"

    return cell[VALEUR]!=None

def isVideCellule(cell:Cellule)->bool:
    """
    Regarde si une celulle est vide ou non
    :param cell: Une cellule (vide ou non)
    :return: Vrai si la cellule est vide, faux sinon
    """
    assert type_cellule(cell), "param cell : mauvais type"

    return cell[VALEUR]==0

def getCouleurCellule(cell:Cellule)->str:
    """
    Regarde la couleur de la cellule cell
    :param cell: Une cellule (vide ou non)
    :return: La couleur de la cellule mise en paramaètre
    """
    assert type_cellule(cell), "param cell : mauvais type"

    return cell[VALEUR]

def  setCouleurCellule(cell:Cellule, nbr:int)->None:
    """
    Attribue une couleur a la cellule cell
    :param cell: Une cellule (vide ou non)
    :param nbr: un entier
    :return: Rien
    """
    assert type_cellule(cell), "param cell : mauvais type"
    assert type(nbr) is int, "param nbr : mauvais type"

    cell[VALEUR]=nbr

    return None

def setNonVuCellule(cell:Cellule)->None:
    """
    L'état de la cellule cell est mis à "non vu"
    :param cell: Une Cellule ( vide ou non)
    :return: Rien
    """
    assert type_cellule(cell), "param cell : mauvais type"

    cell[VALEUR]=None

    return None