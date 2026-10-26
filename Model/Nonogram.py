# Model/Nonogram.py
from Model.CustomTypes import *
from Model.Image import *
from Model.Bloc import *
from Model.Cellule import*
from Model.Joueur import *

def compterBlocsSurLigne(img:ModelImage, ligne:int)->LstBlocs:
    """
    Fait une liste de blocs (1 bloc = 1 couleur) contenus dans la ligne ligne de l'image img
    :param img: un modèle d'image
    :param ligne: un numéro de ligne
    :return: retourne une liste de blocs
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(ligne) is int, "param ligne  : mauvais type"

    liste = []
    nbr = 0
    couleur = None

    for cellule in img[ligne]:
        valeur = cellule[VALEUR]
        if valeur is not None and valeur != 0:
            if valeur == couleur:
                nbr += 1
            else:
                if nbr > 0:
                    liste.append(construireBloc(nbr, couleur))
                couleur = valeur
                nbr = 1
        else:
            if nbr > 0:
                liste.append(construireBloc(nbr, couleur))
                nbr = 0
                couleur = None
    if nbr > 0:
        liste.append(construireBloc(nbr, couleur))

    return liste

def getBlocsLignes(img:Image)->LstLstBlocs:
    """
    Fait une liste de listes de blocs contenus dans l'image img (sur les lignes)
    :param img: une image
    :return: Une liste de listes de blocs
    """
    assert type_image_light(img), "param img : mauvais type"

    liste=[]
    for i in range(len(img)):
        liste.append(compterBlocsSurLigne(img, i))

    return liste

def compterBlocsSurColonne(img:ModelImage, colonne:int)->LstBlocs:
    """
    Fait une liste de blocs contenus dans la colonne colonne de l'image img
    :param img: un modèle d'image
    :param colonne: un numéro de colonne
    :return: retourne une liste de blocs
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(colonne) is int, "param colonne : mauvais type"

    liste = []
    nbr = 0
    couleur = None

    for ligne in img:
        valeur = ligne[colonne][VALEUR]
        if valeur is not None and valeur != 0:
            if valeur == couleur:
                nbr += 1
            else:
                if nbr > 0:
                    liste.append(construireBloc(nbr, couleur))
                couleur = valeur
                nbr = 1
        else:
            if nbr > 0:
                liste.append(construireBloc(nbr, couleur))
                nbr = 0
                couleur = None
    if nbr > 0:
        liste.append(construireBloc(nbr, couleur))

    return liste

def getBlocsColonnes(img:Image)->LstLstBlocs:
    """
    Fait une liste de listes de blocs contenus dans l'image img (sur les colonnes)
    :param img: une image
    :return: Une liste de listes de blocs
    """
    assert type_image_light(img), "param img : mauvais type"

    liste=[]
    for i in range(len(img)):
        liste.append(compterBlocsSurColonne(img, i))

    return liste

def isCouleurCorrecteImage(img:ModelImage, pos:Position, couleur:int)->bool:
    """
    Retourne True si la cellule a bien la couleur couleur, False sinon
    :param img: un modèle d'image
    :param pos: une position dans l'image
    :param couleur: une couleur
    :return: retourne True si la cellule a bien la couleur, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type_position(pos), "param pos : mauvais type"
    assert type(couleur) is int, "param couleur : mauvais type"

    correct = True

    cel=getCellImage(img, pos)
    if cel[VALEUR]!=couleur:
        correct = False
    return correct

def isVuImage(img:PlayerImage)->bool:
    """
    Retourne True si toutes les cellules de l’image du joueur sont découvertes (toutes vues, aucune valeur None), False sinon.
    :param img: Une image du joueur
    :return: True si toutes les cellules de l’image du joueur sont découvertes (toutes vues, aucune valeur None), False sinon.
    """
    assert type_image_light(img), "param img : mauvais type"

    vu=True

    for i in range(len(img)):
        for j in range(len(img[i])):
            pos={LIGNE:i, COLONNE:j}
            if not isVuCellJoueur(img,pos):
                vu=False
    return vu

def reinitialiserImage(img:PlayerImage)->None:
    """
    réinitialise l'image du joueur
    :param img: une image du joueur
    :return: Rien
    """
    assert type_image_light(img), "param img : mauvais type"

    for i in range(len(img)):
        for j in range(len(img[i])):
            pos={LIGNE:i, COLONNE:j}
            setCellImage(img, pos, None)
    return None

def verifierBlocsLigneImage(img: PlayerImage, blocs: LstBlocs, li: int) -> bool:
    """
    Cette fonction vérifie si, sur la ligne correspondante au numéro donné en paramètre, un ou plusieurs blocs a été découvert.
    Si c’est le cas, elle met à jour le bloc correspondant (voir la fonction setVuBloc du fichier Model/Bloc.py)
    :param img:une image de joueur
    :param blocs:une liste de blocs
    :param li: un numéro de ligne
    :return: La fonction retourne True si l’état d’au moins un bloc a été modifié, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    verif=False

    if verifierBlocsLigneImageParLaGauche(img, blocs, li) or verifierBlocsLigneImageParLaDroite(img, blocs, li):
        verif=True
    return verif

def verifierBlocsLigneImageParLaGauche(img: PlayerImage, blocs: LstBlocs, li: int) -> bool:
    """
    Vérifie si la moitié gauche de la ligne li a un ou plusieurs blocs dont l'état est découvert
    :param img: Une image du joueur
    :param blocs: Une liste de blocs
    :param li: un numéro de ligne
    :return: La fonction retourne True si l’état d’au moins un bloc a été modifié, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    verif=False
    col=0
    i=0
    max=len(img) // 2

    while col<max and i<len(blocs):
        if not isVuBloc(blocs[i]) and isVuCellJoueur(img, {LIGNE: li, COLONNE: col}):
            setVuBloc(blocs[i], True)
            verif = True
            i+=1
        col+=1
    return verif


def verifierBlocsLigneImageParLaDroite(img: PlayerImage, blocs: LstBlocs, li: int) -> bool:
    """
    Vérifie si la moitié droite de la ligne li a un ou plusieurs blocs dont l'état est découvert
    :param img: Une image du joueur
    :param blocs: Une liste de blocs
    :param li: uun numéro de ligne
    :return: La fonction retourne True si l’état d’au moins un bloc a été modifié, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"


    verif=False
    col=len(img)-1
    i=len(blocs)-1
    min=len(img) // 2

    while col>=min and i>=0:
        if not isVuBloc(blocs[i]) and isVuCellJoueur(img, {LIGNE: li, COLONNE: col}):
            setVuBloc(blocs[i], True)
            verif = True
            i-=1
        col-=1
    return verif


def verifierBlocsColonneImage(img: PlayerImage, blocs: LstBlocs, col: int)->bool:
    """
    Cette fonction vérifie si, sur la colonne correspondante au numéro donné en paramètre, un ou plusieurs blocs a été découvert.
    Si c’est le cas, elle met à jour le bloc correspondant (voir la fonction setVuBloc du fichier Model/Bloc.py)
    :param img: une image du joueur
    :param blocs: une liste de blocs
    :param col: un numéro de colonne
    :return: La fonction retourne True si l’état d’au moins un bloc a été modifié, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param col : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    verif=False

    if verifierBlocsColonneImageParLaGauche(img, blocs, col) or verifierBlocsColonneImageParLaDroite(img, blocs, col):
        verif = True
    return verif

def verifierBlocsColonneImageParLaGauche(img: PlayerImage, blocs: LstBlocs, col: int) -> bool:
    """
    Vérifie si la moitié gauche (ou haute) de la colonne col a un ou plusieurs blocs dont l'état est découvert
    :param img: une image du joueur
    :param blocs: une liste de blocs
    :param col: u numéro de colonne
    :return: La fonction retourne True si l’état d’au moins un bloc a été modifié, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param col : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    verif=False
    li=0
    i=0
    max=len(img) // 2

    while li<max and i<len(blocs):
        if not isVuBloc(blocs[i]) and isVuCellJoueur(img, {LIGNE: li, COLONNE: col}):
            setVuBloc(blocs[i], True)
            verif = True
            i+=1
        li+=1
    return verif


def verifierBlocsColonneImageParLaDroite(img: PlayerImage, blocs: LstBlocs, col: int) -> bool:
    """
    Vérifie si la moitié droite (ou basse) de la colonne col a un ou plusieurs blocs dont l'état est découvert
    :param img: une image du joueur
    :param blocs: une liste de blocs
    :param col: un numéro de colonne
    :return: La fonction retourne True si l’état d’au moins un bloc a été modifié, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param col : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    verif=False
    li=len(img)-1
    i=len(blocs)-1
    max=len(img) // 2

    while li>=max and i>=0:
        if not isVuBloc(blocs[i]) and isVuCellJoueur(img, {LIGNE: li, COLONNE: col}):
            setVuBloc(blocs[i], True)
            verif = True
            i-=1
        li-=1
    return verif

def isLigneDecouverteImage(img: PlayerImage, blocs: LstBlocs, li: int) -> bool:
    """
    Regarde si la ligne li de l'image img a tout ses blocs découverts ou non
    :param img: Une image du joueur
    :param blocs: une liste de blocs de l'image img
    :param li: un numéro de ligne
    :return:La fonction retourne True si tous les blocs sont découverts sur cette ligne, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    decouverte=False

    Sblocs = 0
    for bloc in blocs:
        Sblocs += bloc[NOMBRE]

    Scellules = 0
    for col in range(len(img)):
        if isVuCellule(img[li][col]) and not isVideCellule(img[li][col]):
            Scellules += 1

    if Sblocs == Scellules:
        decouverte = True

    return decouverte

def getCellsNonVuesLigneImage(img: PlayerImage, li: int) -> list[int]:
    """
    Cette fonction retourne la liste des numéros de colonne des cellules non découvertes dans la ligne li
    :param img: une image du joueur
    :param li: un numéro de ligne
    :return: une liste de numéros de colonne
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(li) is int, "param li : mauvais type"

    liste=[]

    for col in range(len(img[li])):
        if not isVuCellJoueur(img, {LIGNE: li, COLONNE: col}):
            liste.append(col)

    return liste


def isColonneDecouverteImage(img: PlayerImage, blocs: LstBlocs, col: int) -> bool:
    """
    Regarde si la colonne li de l'image img a tout ses blocs découverts ou non
    :param img: Une image du joueur
    :param blocs: une liste de blocs de l'image img
    :param col: un numéro de colonne
    :return:La fonction retourne True si tous les blocs sont découverts sur cette colonne, False sinon
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param col : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for bloc in blocs:
        assert type_bloc(bloc), "param blocs : mauvais type"

    decouverte=False

    Sblocs = 0
    for bloc in blocs:
        Sblocs += bloc[NOMBRE]
    Scellules = 0
    for li in range(len(img)):
        if isVuCellule(img[li][col]) and not isVideCellule(img[li][col]):
            Scellules += 1
    if Sblocs == Scellules:
        decouverte = True

    return decouverte

def getCellsNonVuesColonneImage(img: PlayerImage, col: int) -> list[int]:
    """
    Cette fonction retourne la liste des numéros de ligne des cellules non découvertes dans la ligne col
    :param img: une image du joueur
    :param col: un numéro de colonne
    :return: une liste de numéros de ligne
    """
    assert type_image_light(img), "param img : mauvais type"
    assert type(col) is int, "param col : mauvais type"

    liste=[]

    for li in range(len(img)):
        if not isVuCellJoueur(img, {LIGNE: li, COLONNE: col}):
            liste.append(col)

    return liste

def getNbParCouleur(taille:int, blocs:LstLstBlocs)->NbParCouleur:
    """
    DOnne le dictionnaire associant à chaque couleur le nombre de cellules portant cette couleur
    :param taille:
    :param blocs:
    :return: un dictionnaire de couleurs associé au nombre de cellules ayant une même couleur
    """
    assert type(taille) is int, "param taille : mauvais type"
    assert type(blocs) is list, "param blocs : mauvais type"
    for listeBlocs in blocs: # assert type(blocs) is LstLstBlocs ne marche pas
        assert type(listeBlocs) is list, "param blocs : mauvais type"
        for bloc in listeBlocs:
            assert type_bloc(bloc), "param blocs : mauvais type"

    nbrCouleur = {}
    total = 0

    for listeBlocs in blocs:
        for bloc in listeBlocs:
            couleur = getCouleurBloc(bloc)
            nbr = getNombreBloc(bloc)
            if couleur not in nbrCouleur:
                nbrCouleur[couleur] = 0
            nbrCouleur[couleur] += nbr
            total += nbr
    nbrCouleur[0]=(taille**2)-total

    return nbrCouleur

def getCouleursVuImage(img: PlayerImage, nbrCouleur: NbParCouleur) -> LstCouleurs:
    """
    retourne dans une liste (type/alias LstCouleurs) les couleurs pour lesquelles toutes les cellules
    portant cette couleur sont « découvertes »
    :param img:une image du joueur
    :param nbrCouleur:un dictionnaire de nombre par couleurs
    :return: une liste de couleurs
    """
    assert type_image_light(img), "param img : mauvais type"
    for couleur in nbrCouleur: #assert type(nbrCouleur) is NbParCouleur ne fonctionne pas
        assert type(couleur) is int, "param nbParCouleur : mauvais type"
        assert type(nbrCouleur[couleur]) is int, "param nbParCouleur : mauvais type"

    couleurs = []

    for couleur in nbrCouleur:
        nbrVu = 0
        for i in range(len(img)):
            for j in range(len(img[i])):
                if img[i][j][VALEUR] == couleur:
                    nbrVu += 1
        if nbrVu == nbrCouleur[couleur]:
            couleurs.append(couleur)

    return couleurs