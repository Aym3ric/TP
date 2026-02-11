"""
Module définissant un noeud.
"""
class Noeud:
    """
    Classe représentant un élément (noeud) d'un arbre.
    """
    def __init__(self, val):
        self.val = val
        self.gauche = None
        self.droite = None
