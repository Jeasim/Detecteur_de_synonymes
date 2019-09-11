import re
import DAO as dao
from time import time
import sys

class Lecteur:
    def __init__(self):
        self.stopList = {"lorsque","toute","ah","ainsi","car","chez","non","eux","venait","celui","au","aux","suis","oui","dont","bien","faire","y","avez","ai","j","m","cette","on","moi","me","c","a","plus","qu","dit","de","moi","n","avait","ne","se","était","s","lui","une","l","à","d","un","avait","alors", "au", "aucuns", "aussi", "autre", "avant", "avec", "avoir", "bon", "cas", "ce", "cela", "ces","ces","chaque","ci","comme","comment","dans","des","du","dedans","dehors","depuis","devrait","doit","donc","elle","elles","en","encore","est","et","eu","fait","faites","font","hors","ici","il","ils","je","juste","la","le","les","leur","là","ma","maintenant","mais","mes","mine","moins","mon","même","ni","notre","nous","ou","où","par","parce","pas","peut","peu","plupart","pour","pourquoi","quand","que","quel","quelle","quelles","quels","qui","sa","sans","ses","seulement","si","sien","son","sont","sous","soyez","sur","ta","tandis","tellement","tels","tes","ton","tous","tout","trop","très","tu","voient","vont","votre","vous","vu","ça","étaient","étions","été","être"}
        self.tableauDeMots = []
        self.dictionnaire = {}  
        self.bd = dao.DAO();
        self.dictMotsDB = self.bd.creerDictMotsExistants()
        self.listeNouveauxMotsBD = []
        self.dictMotsMisAJour = {}
      
    def extraire(self, chemin, encodage):
        f = open(chemin, 'r', encoding = encodage)
        texte = f.read()
        
        return texte
        
    def separerMots(self, texte):
        return re.findall('\w+', texte)
    
    def ajouterAuTableau(self, tableauTexte):
        for mot in tableauTexte:
            self.tableauDeMots.append(mot)
    
    def nombreMots(self, texte):
        return len(re.findall('\w+', texte))
    
    def remplirDictionnaire(self):
        compteur = len(self.dictionnaire)
        
        for i in range(len(self.tableauDeMots)):
            if self.tableauDeMots[i] not in self.dictionnaire:
                self.peuplerDictNouveauxMots(self.tableauDeMots[i])
                self.dictionnaire[self.tableauDeMots[i]] = compteur
                compteur += 1
    
    def peuplerDictNouveauxMots(self, mot):
        if mot not in self.dictMotsDB:
            self.listeNouveauxMotsBD.append((len(self.dictMotsDB), mot))
            self.dictMotsDB[mot] = len(self.dictMotsDB)          
    
    def trierInsertUpdate(self, dictionnaireExistant, dictMotsMisAJour):
        listeInsertion = []
        listeUpdate = []
        for cle, nbCoo in dictMotsMisAJour.items():
            mot1, mot2, tailleFenetre = cle
            if cle in dictionnaireExistant:
                if nbCoo != dictionnaireExistant[cle]:
                    listeUpdate.append((nbCoo, mot1, mot2, tailleFenetre))
            else:
                listeInsertion.append((mot1, mot2, tailleFenetre, nbCoo))
        
        return (listeInsertion, listeUpdate)        
             
            
    def definirLangue(self, langue):
        if langue == '0':
            self.langue = "français"
            self.stopList = {"lorsque","toute","ah","ainsi","car","chez","non","eux","venait","celui","au","aux","suis","oui","dont","bien","faire","y","avez","ai","j","m","cette","on","moi","me","c","a","plus","qu","dit","de","moi","n","avait","ne","se","était","s","lui","une","l","à","d","un","avait","alors", "au", "aucuns", "aussi", "autre", "avant", "avec", "avoir", "bon", "cas", "ce", "cela", "ces","ces","chaque","ci","comme","comment","dans","des","du","dedans","dehors","depuis","devrait","doit","donc","elle","elles","en","encore","est","et","eu","fait","faites","font","hors","ici","il","ils","je","juste","la","le","les","leur","là","ma","maintenant","mais","mes","mine","moins","mon","même","ni","notre","nous","ou","où","par","parce","pas","peut","peu","plupart","pour","pourquoi","quand","que","quel","quelle","quelles","quels","qui","sa","sans","ses","seulement","si","sien","son","sont","sous","soyez","sur","ta","tandis","tellement","tels","tes","ton","tous","tout","trop","très","tu","voient","vont","votre","vous","vu","ça","étaient","étions","été","être"}

        
    def motStopList(self, mot):
        if mot in self.stopList:
            return 1
        else:
            return 0
