import numpy as np

class Algorithmie:  
    
    def calculresultats(self, choixMethode, indexMot, mot, matrice, dictTousMots):
        
        tableauResultats = []
    
        indexRangeeMotParametre = dictTousMots[mot]

        rangeeMatrice = matrice[indexRangeeMotParametre]
        
        if choixMethode == '0':
            algo = self.produitScalaire
        elif choixMethode == '1':
            algo = self.leastSquares
        elif choixMethode == '2':
            algo = self.cityBlock
            
        for synonyme, index in dictTousMots.items():
            rangeeMotAnalyse = matrice[index]
            resultat = algo(rangeeMatrice, rangeeMotAnalyse)
            tableauResultats.append((synonyme, resultat))
              
        tableauResultats = self.sortTableau(choixMethode, tableauResultats)
        return tableauResultats
    
    def produitScalaire(self, rangeeMotParametre, rangeeMotAnalyse):
        return np.dot(rangeeMotParametre, rangeeMotAnalyse)
    
    def leastSquares(self, rangeeMotParametre, rangeeMotAnalyse):
        return np.sum((rangeeMotParametre - rangeeMotAnalyse)**2)

    def cityBlock(self, rangeeMotParametre, rangeeMotAnalyse):
        return np.sum(np.abs(rangeeMotParametre - rangeeMotAnalyse))    
    
    
    def sortTableau(self, choixMethode, tableauResultats):
        if choixMethode == '0':
            return sorted(tableauResultats, key=lambda resultat: resultat[1], reverse=True)
        else:
            return sorted(tableauResultats, key=lambda resultat: resultat[1])
        
