"""
Module définissant l'interface Collection.
"""
from abc import ABC, abstractmethod

class Collection(ABC):
    """
    Interface abstraite pour les structures de données.
    """

    @abstractmethod
    def add(self, item):
        """Ajoute un élément à la collection."""
        pass

    @abstractmethod
    def remove(self, item=None):
        """Retire un élément de la collection."""
        pass

    @abstractmethod
    def get(self):
        """Récupère un élément ou une représentation de la collection."""
        pass

    @abstractmethod
    def is_empty(self):
        """Vérifie si la collection est vide."""
        pass
