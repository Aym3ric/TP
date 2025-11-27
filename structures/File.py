from structures.Maillon import Maillon

class File:
    def __init__(self):
        self.tete = None  
        self.queue = None 

    def est_vide(self):
        return self.tete is None

    def enfiler(self, data):
        """Ajoute un élément à la fin de la file."""
        nouveau = Maillon(data)
        
        if self.est_vide():
            self.tete = nouveau
            self.queue = nouveau
        else:
            self.queue.set_suiv(nouveau)
            self.queue = nouveau

    def defiler(self):
        """Retire et retourne l'élément en tête de file (FIFO)."""
        if self.est_vide():
            return None
        
        maillon_tete = self.tete
        valeur = maillon_tete.val
        
        # La tête avance au suivant
        self.tete = maillon_tete.get_suiv()
        
        # Si la file devient vide, on nettoie la queue aussi
        if self.tete is None:
            self.queue = None
            
        return valeur