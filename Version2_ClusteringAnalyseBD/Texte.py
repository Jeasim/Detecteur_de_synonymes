class Texte:
    def __init__(self, chemin, encodage, lecteur):
        self.contenu = lecteur.extraire(chemin, encodage)
        self.contenu = self.contenu.casefold()
        self.tableauContenu = lecteur.separerMots(self.contenu)
        self.nombreDeMots = lecteur.nombreMots(self.contenu)
       
    