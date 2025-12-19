from structures.Maillon import Maillon
from structures.Collection import Collection

class LinkedList(Collection):
    def __init__(self, first_maillon: Maillon = None):
        self.first_maillon = first_maillon

    def is_empty(self):
        return self.first_maillon is None
    
    def add(self, item):
        maillon = item if isinstance(item, Maillon) else Maillon(item)
        self.add_maillon(maillon)

    def remove(self, item):
        self.delete_maillon(item)
    
    def get(self):
        return self.to_list()

    def get_last(self):
        if self.is_empty():
            return None
        courant = self.first_maillon
        while courant.get_suiv() is not None:
            courant = courant.get_suiv()
        return courant

    def add_maillon(self, maillon: Maillon):
        if self.is_empty():
            self.first_maillon = maillon
            return
        self.get_last().set_suiv(maillon)

    def delete_maillon(self, val):
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
        elements = []
        courant = self.first_maillon
        while courant is not None:
            elements.append(courant.val)
            courant = courant.get_suiv()
        return elements