from structures.Maillon import Maillon
from structures.Collection import Collection

class File(Collection):
    def __init__(self):
        self.tete = None  
        self.queue = None 

    def is_empty(self):
        return self.tete is None

    def add(self, item):
        # Enfiler
        self.enfiler(item)

    def remove(self, item=None):
        # Defiler (FIFO)
        return self.defiler()
        
    def get(self):
        return self.tete.val if self.tete else None

    def est_vide(self):
        return self.is_empty()

    def enfiler(self, data):
        nouveau = Maillon(data)
        if self.is_empty():
            self.tete = nouveau
            self.queue = nouveau
        else:
            self.queue.set_suiv(nouveau)
            self.queue = nouveau

    def defiler(self):
        if self.is_empty():
            return None
        
        maillon_tete = self.tete
        valeur = maillon_tete.val
        
        self.tete = maillon_tete.get_suiv()
        
        if self.tete is None:
            self.queue = None
            
        return valeur