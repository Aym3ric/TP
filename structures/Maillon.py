class Maillon:
    def __init__(self, val=None):
        self.val = val
        self.suiv = None

    def est_vide(self):
        return self.val is None and self.suiv is None
    
    def get_value(self):
        return self.val

    def get_suiv(self):
        return self.suiv

    def set_suiv(self, suivant):
        self.suiv = suivant