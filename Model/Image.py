# Model/Image.py

from Model.CustomTypes import Image
from Model.Cellule import *
from Model.Position import *

#
# Gestion simple des nonograms
#
# Accès simple en lecture et en écriture à une "image"
# Création d'une "image"...
#


def type_image_light(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    Version light : Ne vérifie pas le contenu des listes...

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if type(img) is not list:
        return False
    wrong = "Erreur !"
    if len(img) == 0:
        return False
    if type(img[0]) is not list:
        return False
    n_c = len(img[0])
    if n_c != len(img):
        return False
    if next((wrong for line in img if type(line) is not list or len(line) != n_c), True) == wrong:
        return False
    return True


def type_image_full(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    En plus de la version light, vérifie que le contenu des listes correspond bien à une cellule.

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if not type_image_light(img):
        return False
    wrong = "Erreur !"
    if next((wrong for line in img for c in line if c is not None and not type_cellule(c)), True) == wrong:
        return False
    return True

"""
RAPPEL:

Cellule = dict[str, int | None]

Image = list[list[Cellule]]

Position = dict[str, int] avec LIGNE et COLONNE
"""


def getCellImage(img:Image,pos:Position) -> Cellule:
    """
    Sert à récupérer la cellule à la position pos dans l'image img
    :param img: Une image
    :param pos: Une position
    :return: Une cellule
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type_position(pos), "param pos : mauvais type"

    ligne = getLignePosition(pos)
    colonne = getColonnePosition(pos)

    return img[ligne][colonne]

def setCellImage(img: Image, pos: Position, nbr: int | None) -> None:
    """
    Changer la couleur de la cellule dans l'image img à la position pos par l'entier nbr
    :param pos: Une position
    :param img: Une image
    :param nbr: Un entier ou None
    :return: Rien
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type_position(pos), "param pos : mauvais type"
    assert nbr is None or type(nbr) is int, "param nbr : mauvais type"

    ligne = getLignePosition(pos)
    colonne = getColonnePosition(pos)

    img[ligne][colonne][VALEUR] = nbr
    return None

def creerImage(nbr:int, liste: list[list[int]] | None=None)->Image:
    """
    Créer une image de taille nbr
    :param nbr: entier correspondant à la taille de l'image
    :param liste: une liste de liste d'entier
    :return: une image
    """
    assert type(nbr) is int, "param nbr : mauvais type"
    assert liste is None or type(liste) is list, "param liste : mauvais type"
    assert 5 <= nbr <= 20, "param nbr : la taille de l'image doit être comprise entre 5 et 20"
    if liste is not None:
        assert len(liste) == nbr, "param liste : taille pas egal à nbr"
        for ligne in liste:
            assert type(ligne) is list, "param liste : pas un liste de listes"
            assert len(ligne) == nbr, "param liste : les lignes doivent etre égal à nbr"

    img = []

    for l in range(nbr):
        ligne = []
        for c in range(nbr):
            cel = construireCellule()
            if liste is not None:
                valeur = liste[l][c]
                if valeur is not None:
                    setCouleurCellule(cel, valeur)
            ligne.append(cel)
        img.append(ligne)

    return img
