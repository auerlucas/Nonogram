# Model/Suggestion.py

# Suggestions de coups à jouer modélisés par un dictionnaire à deux clés :
# - POSITION : Position dans l'image
# - COULEUR : Couleur à placer (la couleur transparente, 0, étant acceptée)

# Deux clés associées au dictionnaire représentant une suggestion :
POSITION = "position"
COULEUR = "couleur"


from Model.CustomTypes import *
from Model.Position import *

def type_suggestion(suggestion: Suggestion) -> bool:
    """
    Détermine si le paramètre correspond ou non à une suggestion

    :param suggestion: Objet à tester
    :return: True s'il correspond à une suggestion, False sinon
    """
    if type(suggestion) is not dict:
        return False
    if POSITION not in suggestion or COULEUR not in suggestion:
        return False
    if not type_position(suggestion[POSITION]):
        return False
    if type(suggestion[COULEUR]) is not int:
        return False
    return True

def construireSuggestion(pos:Position, couleur:int)->Suggestion:
    """
    Construit un dictionnaire {POSITION:COULEUR} correspondant à une suggestion
    :param pos: Une position
    :param couleur: Un entier correspondant à une couleur
    :return: retourne un dictionnaire
    """
    assert type_position(pos), "param pos : mauvais type"
    assert type(couleur) is int, "param couleur : mauvais type"

    return {POSITION: pos, COULEUR: couleur}

def getPositionSuggestion(sugg:Suggestion)->Position:
    """
    DOnne une position contenu dans une suggestion sugg
    :param sugg: Une suggestion
    :return: retourne une position
    """
    assert type_suggestion(sugg), "param sugg : mauvais type"

    return sugg[POSITION]

def getCouleurSuggestion(sugg:Suggestion)->int:
    """
    Donne une couleur contenu dans une suggestion sugg
    :param sugg: une suggestion
    :return: un entier correspondant à une couleur
    """
    assert type_suggestion(sugg), "param sugg : mauvais type"

    return sugg[COULEUR]



