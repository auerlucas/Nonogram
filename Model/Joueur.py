# Model/Joueur.py
from typing import assert_type

from Model.CustomTypes import *
from Model.Image import *
from Model.Cellule import *
from Model.Bloc import *
from Model.Suggestion import *
from Model.Nonogram import *

def isVuCellJoueur(img:PlayerImage, pos:Position)->bool:
    """
    Savoir si une cellule a été vu ou non sur l'image du joueur
    :param img: une image du joueur
    :param pos: Une position dans l'image img
    :return: True si la cellule correspondant à la position a été découverte, False sinon
    """
    assert type_position(pos), "param pos : mauvais type"

    vu=False

    cel = getCellImage(img, pos)
    if cel[VALEUR] is not None:
        vu = True
    return vu

def isLigneNonVueImage(img:PlayerImage, li:int)->bool:
    """
    Retourne True si la ligne ne possède aucune cellule découverte, False sinon.
    :param img: une image du joueur
    :param li: un numéro de ligne
    :return: Retourne True si la ligne ne possède aucune cellule découverte, False sinon.
    """
    assert type_image_light(img), "param img : une image du joueur"
    assert type(li) is int, "param li : mauvais param"

    nonVu=True
    col=0

    while nonVu or col!=len(img):
        if isVuCellJoueur(img, img[li][col]):
            nonVu=False
        col+=1

    return nonVu

def isColonneNonVueImage(img:PlayerImage, col:int)->bool:
    """
    Retourne True si la colonne ne possède aucune cellule découverte, False sinon.
    :param img: une image du joueur
    :param col: un numéro de colonne
    :return: Retourne True si la colonne ne possède aucune cellule découverte, False sinon.
    """
    assert type_image_light(img), "param img : une image du joueur"
    assert type(col) is int, "param col: mauvais param"

    nonVu=True
    li=0

    while nonVu or col!=len(img):
        if isVuCellJoueur(img[li][col]):
            nonVu=False
        li+=1

    return nonVu

def appliquerMonoRecouvrementLigne(img:PlayerImage, li:int, blocs:LstBlocs)->LstSuggestions:
    """
    Retourne une liste de suggestions
    :param img:une image du joueur
    :param li:un numéro de ligne
    :param blocs:une liste de blocs
    :return:retourne une liste de suggestions
    """
    assert type_image_light(img), "param img : une image du joueur"
    assert type(li) is int, "param li : mauvais param"
    assert type(blocs) is list, "param blocs : mauvais param"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais param"

    suggs=[]
    col=0
    n =len(img[li])

    for bloc in blocs:
        taille=getNombreBloc(bloc)
        debut= max(col, n-taille)
        fin =min(col+taille, n)
        for i in range(debut, fin):
            suggs.append(construireSuggestion({LIGNE:li, COLONNE:i}, getCouleurBloc(bloc)))
        col+=taille + 1

    return suggs

def appliquerMonoRecouvrementColonne(img:PlayerImage, col:int, blocs:LstBlocs)->LstSuggestions:
    """
    Retourne une liste de suggestions
    :param img:une image du joueur
    :param li:un numéro de colonne
    :param blocs:une liste de blocs
    :return:retourne une liste de suggestions
    """
    assert type_image_light(img), "param img : une image du joueur"
    assert type(col) is int, "param colonne : mauvais param"
    assert type(blocs) is list, "param blocs : mauvais param"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais param"

    suggs=[]
    li=0
    n =len(img)

    for bloc in blocs:
        taille=getNombreBloc(bloc)
        debut= max(li, n-taille)
        fin =min(li +taille, n)
        for i in range(debut, fin):
            suggs.append(construireSuggestion({LIGNE:li, COLONNE:i}, getCouleurBloc(bloc)))
        li+= taille + 1

    return suggs

def appliquerMonoRecouvrement(img:PlayerImage, blocsLi:LstLstBlocs, blocsCol:LstLstBlocs)->LstSuggestions:
    """

    :param img:
    :param blocsLi:
    :param blocsCol:
    :return:
    """
    assert type_image_light(img), "param img : une image du joueur"
    assert type(blocsLi) is list, "param blocsLi : mauvais param"
    for blocs in blocsLi: # assert type(blocs) is LstLstBlocs ne marche pas
        assert type(blocs) is list, "param blocsLi : mauvais type"
        for bloc in blocs:
            assert type_bloc(bloc), "param blocsLi : mauvais type"
    assert type(blocsCol) is list, "param blocsCol : mauvais param"
    for blocs in blocsCol: # assert type(blocs) is LstLstBlocs ne marche pas
        assert type(blocs) is list, "param blocsCol : mauvais type"
        for bloc in blocs:
            assert type_bloc(bloc), "param blocsCol : mauvais type"

    suggs=[]

    for i in range(len(img)):
        suggs+= appliquerMonoRecouvrementLigne(img, i, blocsLi[i])
        suggs +=appliquerMonoRecouvrementColonne(img, i, blocsCol[i])

    return suggs

def isRangeeVide(rangee:Rangee)->bool:
    """

    :param rangee:
    :return:
    """
    assert type(rangee) is list, "param rangee : mauvais param"
    for cell in rangee:
        assert type_cellule(cell), "param rangee : mauvais param"

    vu=True

    for cell in rangee:
        if isVuCellule(cell):
            return False

    return vu

def isRangeeDecouverte(rangee:Rangee)->bool:
    """

    :param rangee:
    :return:
    """
    assert type(rangee) is list, "param rangee : mauvais param"
    for cell in rangee:
        assert type_cellule(cell), "param rangee : mauvais param"

    decouverte=True

    for cell in rangee:
        if not isVuCellule(cell):
            decouverte=False

    return decouverte

def appliquerMonoGlueBordRangee(rangee:Rangee, blocs:LstBlocs)->LstIndexCouleurs:
    """
    Cette fonction applique la « glue du bord » sur le bord gauche de la ligne et retourne les « suggestions trouvées » dans une liste
    :param rangee: une liste de cellules
    :param blocs: une liste de blocs
    :return:liste d'index de couleurs
    """
    assert type(rangee) is list, "param rangee : mauvais param"
    for cell in rangee:
        assert type_cellule(cell), "param rangee : mauvais param"
    assert type(blocs) is list, "param blocs : mauvais param"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais param"

    suggs=[]

    if not isRangeeVide(rangee) and not isRangeeDecouverte(rangee):
        for i in range(getNombreBloc(blocs[0])):
            if not isVuCellule(rangee[i]):
                suggs.append((i, getCouleurBloc(blocs[0])))

    return suggs

def getLigneImage(img: PlayerImage, li: int) -> Rangee:
    """
    Retourne la ligne li de l'image
    :param img: Image du joueur
    :param li: Numéro de ligne
    :return: La ligne sous forme de Rangee
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"

    ligne=img[li]
    return ligne


def getLigneInverseImage(img: PlayerImage, li: int) -> Rangee:
    """
    Retourne la ligne li inversée de l'image
    :param img: Image du joueur
    :param li: Numéro de ligne
    :return: Ligne inversée (Rangee)
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"

    ligne =getLigneImage(img, li)
    inverse= list(reversed(ligne))

    return inverse


def getColonneImage(img: PlayerImage, col: int) -> Rangee:
    """
    Retourne la colonne co de l'image
    :param img: Image du joueur
    :param col: Numéro de colonne
    :return: Colonne sous forme de Rangee
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param co : mauvais type"

    co=[]

    for li in range(len(img)):
        co.append(img[li][col])
    return co


def getColonneInverseImage(img: PlayerImage, col: int) -> Rangee:
    """
    Retourne la colonne col inversée de l'image
    :param img: Image du joueur
    :param col: Numéro de colonne
    :return: Colonne inversée (Rangee)
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param co : mauvais type"

    col=getColonneImage(img, col)
    inverse= list(reversed(col))

    return inverse


def getLstBlocsInverse(blocs: LstBlocs) -> LstBlocs:
    """
    Retourne la liste de blocs inversé
    :param blocs: Liste de blocs (LstBlocs)
    :return: Liste inversée
    """
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    inverse=list(reversed(blocs))
    return inverse


def getIndexInverseDeIndexCouleurs(iCouleurs: LstIndexCouleurs, dim: int) -> LstIndexCouleurs:
    """
    Calcule les indices réels d'une rangée ou colonne inversée
    :param iCouleurs: Liste d'indices et couleurs (LstIndexCouleurs)
    :param dim: Dimension de la rangée ou colonne
    :return: Liste d'indices corrigés (LstIndexCouleurs)
    """
    assert type(iCouleurs) is list, "param idx_color : mauvais type"
    assert type(dim) is int, "param dim : mauvais type"

    resultat=[]

    for i, couleur in iCouleurs:
        I =dim-1-i
        resultat.append((I, couleur))
    return resultat

def indexCouleursToSuggestions(iCouleurs: LstIndexCouleurs, n: int, isLi: bool) -> LstSuggestions:
    """
    Transforme une liste de tuples (indice, couleur) en liste de suggestions
    :param iCouleurs: liste de tuples (index, couleur)
    :param n: numéro de ligne ou colonne
    :param isLi: True si ligne, False si colonne
    :return: liste de suggestions
    """
    assert type(iCouleurs) is list, "param iCouleurs: mauvais type"
    assert type(n) is int, "param n : mauvais type"
    assert type(isLi) is bool, "param isLi : mauvais type"

    suggs=[]

    for pair in iCouleurs:
        pos={}
        if isLi:
            pos[LIGNE]= n
            pos[COLONNE]=pair[0]
        else:
            pos[LIGNE]=pair[0]
            pos[COLONNE]=n
        suggs.append(construireSuggestion(pos, pair[1]))

    return suggs

def appliquerMonoGlueBord(img: PlayerImage, blocsLi: LstLstBlocs, blocsCol: LstLstBlocs) -> LstSuggestions:
    """
    Donne une liste de toutes les suggestions
    :param img:une image du joueur
    :param blocsLi:une liste de blocs de lignes
    :param blocsCol: une liste de blocs de colonne
    :return: une liste de suggestions
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(blocsLi) is list, "param blocsLi : mauvais param"
    for blocs in blocsLi: # assert type(blocs) is LstLstBlocs ne marche pas
        assert type(blocs) is list, "param blocsLi : mauvais type"
        for bloc in blocs:
            assert type_bloc(bloc), "param blocsLi : mauvais type"
    assert type(blocsCol) is list, "param blocsCol : mauvais param"
    for blocs in blocsCol: # assert type(blocs) is LstLstBlocs ne marche pas
        assert type(blocs) is list, "param blocsCol : mauvais type"
        for bloc in blocs:
            assert type_bloc(bloc), "param blocsCol : mauvais type"

    suggs=[]
    n=len(img)

    for i in range(n):
        suggs+=indexCouleursToSuggestions(appliquerMonoGlueBordRangee(getLigneImage(img, i), blocsLi[i]), i, True)
        suggs+=indexCouleursToSuggestions(getIndexInverseDeIndexCouleurs(appliquerMonoGlueBordRangee(getLigneInverseImage(img, i), getLstBlocsInverse(blocsLi[i])), n), i, True)
        suggs+=indexCouleursToSuggestions(appliquerMonoGlueBordRangee(getColonneImage(img, i), blocsCol[i]), i, False)
        suggs+= indexCouleursToSuggestions(getIndexInverseDeIndexCouleurs(appliquerMonoGlueBordRangee(getColonneInverseImage(img, i), getLstBlocsInverse(blocsCol[i])), n), i, False)

    return suggs

def appliquerBoucheTrouRangee(rangee: Rangee, blocs: LstBlocs) -> LstSuggestions:
    """
    Bouche les trous d'une rangée rangee
    :param rangee:une rangée
    :param blocs:une liste de blocs
    :return:une liste de suggestions
    """
    minBloc=None

    for b in blocs:
        n=getNombreBloc(b)
        if minBloc is None or n<minBloc:
            minBloc= n

    suggs=[]
    trou= []

    i =0
    while i <len(rangee):
        if rangee[i][VALEUR]==0:
            trou.append(i)
        else:
            if len(trou)< minBloc:
                suggs.append(construireSuggestion({LIGNE: 0, COLONNE: i}, 0))
            trou = []
        i += 1
    return suggs