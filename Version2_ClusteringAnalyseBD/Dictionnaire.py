import numpy as np

class Dictionnaire:
    def __init__(self, tailleFenetre, tableau, dictionnaireMotsUniques):
        self.dictionnaireCooccurences = {}
        self.tailleFenetre = int(tailleFenetre)
        self.tableauTexteInitial = tableau
        self.nombreDeMots = len(tableau)
        self.dictionnaireMotsUniques = dictionnaireMotsUniques

    
    def construireDictionnaireCooccurences(self):
            minFenetre = int(-(np.floor(self.tailleFenetre / 2)))
            maxFenetre = int(np.ceil(self.tailleFenetre / 2))
            index = self.tailleFenetre + minFenetre - 1
            
            while index <= self.nombreDeMots - maxFenetre:
                mot = self.tableauTexteInitial[index]
                indexDict = self.dictionnaireMotsUniques[mot]
             
                for i in range(minFenetre, maxFenetre):
                    motAnalyse = self.tableauTexteInitial[index + i]
                    indextDictAnalyse = self.dictionnaireMotsUniques[motAnalyse]
                    if indexDict == indextDictAnalyse:
                        pass
                    else:
                        if indextDictAnalyse <= indexDict:
                            if (indexDict, indextDictAnalyse, self.tailleFenetre) not in self.dictionnaireCooccurences:
                                self.dictionnaireCooccurences[(indexDict, indextDictAnalyse, self.tailleFenetre)] = 1
                            else:
                                self.dictionnaireCooccurences[(indexDict, indextDictAnalyse, self.tailleFenetre)] += 1
                        
                index += 1
                
            return self.dictionnaireCooccurences
        