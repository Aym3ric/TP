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

    def est_vide(self):
        """Retourne True si le maillon n'a pas de valeur ni de suivant."""
        return self.val is None and self.suiv is None

    def get_value(self):
        """Retourne la valeur stockée dans le maillon."""
        return self.val

    def get_suiv(self):
        """Retourne le maillon suivant."""
        return self.suiv

    def set_suiv(self, suivant):
        """Définit le maillon suivant."""
        self.suiv = suivant
