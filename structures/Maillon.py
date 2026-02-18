"""
Module définissant un maillon pour les structures chaînées.
"""

class Maillon:
    """
    Classe représentant un élément (maillon) d'une liste chaînée.
    """
    def __init__(self, val=None):
        """Initialise un maillon avec une valeur et un pointeur suivant vide."""
        self.val = val
        self.suiv = None

    def get_suiv(self):
        """Retourne le maillon suivant."""
        return self.suiv

    def set_suiv(self, suivant):
        """Définit le maillon suivant."""
        self.suiv = suivant
