from Maillon import Maillon

class LinkedList:
    def __init__(self, first_maillon: Maillon = None):
        self.first_maillon = first_maillon

    def est_vide(self):
        return self.first_maillon is None
    
    def get_last(self):
        if self.est_vide():
            return None
        
        courant = self.first_maillon
        while courant.get_suiv() is not None:
            courant = courant.get_suiv()
        return courant

    def add_maillon(self, maillon: Maillon):
        # Ajoute un maillon à la fin de la liste
        if self.est_vide():
            self.first_maillon = maillon
            return

        self.get_last().set_suiv(maillon)

    def delete_maillon(self, val):
        # Supprime le premier maillon ayant la valeur donnée
        if self.est_vide():
            return

        # Suppression en tête
        if self.first_maillon.val == val:
            self.first_maillon = self.first_maillon.get_suiv()
            return

        # Recherche du maillon à supprimer
        courant = self.first_maillon
        while courant.get_suiv() is not None:
            if courant.get_suiv().val == val:
                courant.set_suiv(courant.get_suiv().get_suiv())
                return
            courant = courant.get_suiv()
