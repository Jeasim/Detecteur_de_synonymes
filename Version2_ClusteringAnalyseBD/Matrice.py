import numpy as np

class Matrice:
    def __init__(self, dictionnaireMotsExistants):
        self.matriceVide = self.construireMatriceInitiale(len(dictionnaireMotsExistants))
        
    def construireMatriceInitiale(self, tailleDict):
        return np.zeros((tailleDict, tailleDict))      