"""
Module implémentant une liste chaînée simple.
"""
from structures.maillon import Maillon
from structures.collection import Collection

class LinkedList(Collection):
    """
    Implémentation d'une liste chaînée simple héritant de Collection.
    """
    def __init__(self, first_maillon: Maillon = None):
        """Initialise la liste chaînée."""
        self.first_maillon = first_maillon

    def is_empty(self):
        """Retourne True si la liste est vide."""
        return self.first_maillon is None

    def add(self, item):
        """Ajoute un élément à la fin de la liste."""
        maillon = item if isinstance(item, Maillon) else Maillon(item)
        self.add_maillon(maillon)

    def remove(self, item=None):
        """Retire la première occurrence de l'élément spécifié."""
        self.delete_maillon(item)

    def get(self):
        """Retourne la liste sous forme de liste Python standard."""
        return self.to_list()

    def get_last(self):
        """Retourne le dernier maillon de la liste."""
        if self.is_empty():
            return None
        courant = self.first_maillon
        while courant.get_suiv() is not None:
            courant = courant.get_suiv()
        return courant

    def add_maillon(self, maillon: Maillon):
        """Ajoute un maillon à la fin de la liste."""
        if self.is_empty():
            self.first_maillon = maillon
            return
        self.get_last().set_suiv(maillon)

    def delete_maillon(self, val):
        """Supprime la première occurrence d'un maillon ayant la valeur val."""
        if self.is_empty():
            return
        if self.first_maillon.val == val:
            self.first_maillon = self.first_maillon.get_suiv()
            return
        courant = self.first_maillon
        while courant.get_suiv() is not None:
            if courant.get_suiv().val == val:
                courant.set_suiv(courant.get_suiv().get_suiv())
                return
            courant = courant.get_suiv()

    def to_list(self):
        """Convertit la liste chaînée en liste Python."""
        elements = []
        courant = self.first_maillon
        while courant is not None:
            elements.append(courant.val)
            courant = courant.get_suiv()
        return elements
