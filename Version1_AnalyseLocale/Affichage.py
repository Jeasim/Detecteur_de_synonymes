class Affichage:
    
    def __init__(self):
        self.langue = ""

    def afficherResultats(self, nbSynomymes, resultat, mot, motsDansStopList):
        compteur = 0
        index = 0
        while compteur <= nbSynomymes: 
            synonyme, score = resultat[index]
            if motsDansStopList(synonyme) or mot == synonyme:
                index += 1
            else:
                self.afficherLigneResultat(resultat[index])
                index += 1
                compteur += 1
    
           
    def afficherLigneResultat(self, resultat):
        print(resultat)    
    
    def choixLangue(self):
        self.langue = input("Dans quelle langue est votre texte ?\nfrançais : 0, anglais : 1 \n")
        return self.langue
   
    def inputParamsRecherche(self):
        return input("\n\nEntrez un mot, le nombre de synonymes que vous voulez et la méthode de calcul, \ni.e produit scalaire: 0, least squares: 1, cityblock: 2\nTapez q pour quitter ou l pour changer de langue\n\n").split()
    
    def erreurChemin(self):
        print(" ! Encodage non-valide ! ")
        
    def erreurEncodage(self):
        print(" ! Chemin inexistant ! ")   
        
    def erreurTailleFenetre(self):
        print("  ! Taille de fenêtre non-valide ! ") 
    
    def erreurMotInexistant(self):
        print("\n ! Le mot recherché n'existe pas dans le texte !")

    def erreurNombreSynonymes(self):    
        print("\n ! Veuillez entrer un nombre de synonymes valide !")
        
    def erreurChoixAlgo(self):
        print("\n ! Veuillez sélectionner une méthode de recherche valide ! ")    
    
    def erreurNombreParametresRecherche(self):
        print("\n ! Veuillez entrer 3 paramètres ! ")
    
    def tempsEcoule(self, type, temps):
        print("\n{} effectué en {} secondes".format(type, temps))    
        
    def finProgramme(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")