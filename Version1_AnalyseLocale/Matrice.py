import numpy as np

class Matrice:
    def __init__(self, tailleFenetre, tableauMots, dictionnaire):
        self.tableauTexteInitiale = tableauMots
        self.dictionnaire = dictionnaire
        self.nombreDeMots = len(tableauMots)
        self.tailleFenetre = int(tailleFenetre)
        self.matriceCooccurences = self.construireMatriceCooccurences()
        
        
    def construireMatriceInitiale(self):
        return np.zeros((len(self.dictionnaire), len(self.dictionnaire)))
    
    def construireMatriceCooccurences(self):
        matrice = self.construireMatriceInitiale()
        minFenetre = int(-(np.floor(self.tailleFenetre / 2)))
        maxFenetre = int(np.ceil(self.tailleFenetre / 2))
        index = self.tailleFenetre + minFenetre - 1
        
        while index <= self.nombreDeMots - maxFenetre:
            
            mot = self.tableauTexteInitiale[index]
            indexDict = self.dictionnaire[mot]
         
            for i in range(minFenetre, maxFenetre):
                motAnalyse = self.tableauTexteInitiale[index + i]
                if mot == motAnalyse:
                    pass
                else:
                    indexDictMotCoo = self.dictionnaire[self.tableauTexteInitiale[index + i]]
                    matrice[indexDict][indexDictMotCoo] += 1
                    
            index += 1
            
        return matrice
        
                