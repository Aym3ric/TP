"""
Module implémentant une File (Queue) FIFO.
"""
from structures.maillon import Maillon
from structures.collection import Collection

class File(Collection):
    """
    Implémentation d'une File (FIFO) héritant de Collection.
    """
    def __init__(self):
        """Initialise une file vide."""
        self.tete = None
        self.queue = None

    def is_empty(self):
        """Retourne True si la file est vide."""
        return self.tete is None

    def add(self, item):
        """Enfile un élément."""
        self.enfiler(item)

    def remove(self, item=None):
        """Défile un élément (FIFO). L'argument item est ignoré."""
        return self.defiler()

    def get(self):
        """Retourne la valeur en tête de file sans défiler."""
        return self.tete.val if self.tete else None

    def est_vide(self):
        """Alias pour is_empty."""
        return self.is_empty()

    def enfiler(self, data):
        """Ajoute un élément en queue de file."""
        nouveau = Maillon(data)
        if self.is_empty():
            self.tete = nouveau
            self.queue = nouveau
        else:
            self.queue.set_suiv(nouveau)
            self.queue = nouveau

    def defiler(self):
        """Retire et retourne l'élément en tête de file."""
        if self.is_empty():
            return None

        maillon_tete = self.tete
        valeur = maillon_tete.val

        self.tete = maillon_tete.get_suiv()

        if self.tete is None:
            self.queue = None

        return valeur
