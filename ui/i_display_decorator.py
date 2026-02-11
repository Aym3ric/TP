"""
Interface pour les décorateurs d'affichage.
"""
from abc import ABC, abstractmethod

class IDisplayDecorator(ABC):
    """
    Interface abstraite définissant la méthode show pour l'affichage.
    """
    
    @abstractmethod
    def show(self) -> str:
        """Retourne la représentation sous forme de chaîne de caractères."""

# Decorator
