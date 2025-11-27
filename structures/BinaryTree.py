from Noeud import Noeud

class BinaryTree:
    def __init__(self, racine=None):
        self.racine = racine

    def est_vide(self):
        return self.racine is None

    def inserer(self, val):
        nouveau = Noeud(val)

        if self.est_vide():
            self.racine = nouveau
            return

        # Insertion simple : on cherche la 1ère place libre
        queue = [self.racine]
        while queue:
            courant = queue.pop(0)

            if courant.gauche is None:
                courant.gauche = nouveau
                return
            else:
                queue.append(courant.gauche)

            if courant.droite is None:
                courant.droite = nouveau
                return
            else:
                queue.append(courant.droite)
