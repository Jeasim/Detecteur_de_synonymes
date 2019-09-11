import DAO as dao
import Algorithmie as algo
import numpy as np
import csv
import sys
from time import time
from numpy.random.mtrand import randint

class Clustering:
    def __init__(self, matriceCooccurrences, indiceMotParam, nombreMotsAffiches, nbCentroides=0, estAnalyseVerbale=False):
        self.debut = None
        self.bd = dao.DAO()
        self.dictMotExistant = self.bd.creerDictMotsExistants()
        self.algo = algo.Algorithmie()
        self.nbMots = len(matriceCooccurrences[0])
        self.matriceCooccurrences = matriceCooccurrences
        self.centroidesEnParam = False
        self.estAnalyseVerbale = estAnalyseVerbale
        self.nombreMotsAAfficher = int(nombreMotsAffiches)
        
        if not indiceMotParam == []:
            self.centroidesEnParam = True
            self.nbCentroides= len(indiceMotParam)
        else:
            self.nbCentroides = nbCentroides
        if(self.estAnalyseVerbale):
            self.genererDictionnaireVerbes()
            

    
    def bouclePrincipale(self):
        aucunDeplacement = False
        
        self.debut = time()
        
        matriceCentroides = np.zeros((self.nbCentroides,self.nbMots))
        vectAppartenance = np.zeros(self.nbMots)
        vectAppartenanceSuivant = np.zeros(self.nbMots)
        
        compteurBoucles = 1
        
        if self.centroidesEnParam:
            vectAppartenance = np.zeros(self.nbMots)
            for i in len(self.indexMots):
                matriceCentroides[i] = self.matriceCooccurrences[self.indexMots[i]]
        else:
            vectAppartenance = self.attribuerCentroidesAleatoirement()
            self.afficherNombreCentroideAleatoire(self.nbCentroides)
            matriceCentroides, vectCompteurMotParCentroide = self.calculCentroides(vectAppartenance)
            vectAppartenanceSuivant = self.calculVectAppartenance(matriceCentroides)
            self.afficherResultatParIteration(compteurBoucles, vectCompteurMotParCentroide,self.nbMots)

        while not aucunDeplacement:
            #----------------------------------------------------------------------------------------
            #debutSequence = randint(0, self.nbMots)

            #----------------------------------------------------------------------------------------
            matriceCentroides = np.zeros((self.nbCentroides,self.nbMots))
            
            matriceCentroides,vectCompteurMotParCentroide = self.calculCentroides(vectAppartenance)
            vectAppartenanceSuivant = self.calculVectAppartenance(matriceCentroides)
            
            aucunDeplacement, nbChangement = self.isChangementIterations(vectAppartenance, vectAppartenanceSuivant)
            
            if not aucunDeplacement:     
                vectAppartenance = vectAppartenanceSuivant
            
            compteurBoucles += 1
            
            self.afficherResultatParIteration(compteurBoucles, vectCompteurMotParCentroide, nbChangement)
            
        self.afficherResultatsGroupe(vectAppartenanceSuivant,matriceCentroides)
    
    def calculVectAppartenance(self, matriceCentroides):
        vectAppartenance = np.zeros(self.nbMots)
        
        for indiceMot in range(self.nbMots):
            plusPres = sys.maxsize
            compteur = 0
            vectCooccurrences = self.matriceCooccurrences[indiceMot]

            for vectCentroide in matriceCentroides:
                distance = self.comparerCentroideAvecMot(vectCooccurrences, vectCentroide)
                if distance < plusPres:
                    plusPres = distance
                    indiceCentroidePlusPres = compteur
                compteur += 1
                    
            vectAppartenance[indiceMot] = indiceCentroidePlusPres
                     
        return vectAppartenance
    
    def calculCentroides(self, vectAppartenance):
        matriceCentroides = np.zeros((self.nbCentroides,self.nbMots))
        vectCompteurMotsParCentroide = np.zeros(self.nbCentroides)        
    
        for i in range(len(vectAppartenance)):
            centroide = int(vectAppartenance[i])
            matriceCentroides[centroide] += self.matriceCooccurrences[i]
            vectCompteurMotsParCentroide[centroide] += 1
        
        self.repositionnerCentroide(matriceCentroides, vectCompteurMotsParCentroide)
            
        return matriceCentroides, vectCompteurMotsParCentroide
    
    
        
    def isChangementIterations(self,vectAppartenance,vectAppartenanceSuivant):
        aucunDeplacement = True
        nbChangements = 0
        for index in range(len(vectAppartenance)):
            if vectAppartenance[index]!=vectAppartenanceSuivant[index]:
                nbChangements+=1
                aucunDeplacement=False

        return aucunDeplacement , nbChangements
    
    
    def repositionnerCentroide(self, matriceCentroides, vectCompteurMotsParCentroide):
        for i in range(self.nbCentroides):
            if not vectCompteurMotsParCentroide[i] == 0:
                matriceCentroides[i] = matriceCentroides[i] / vectCompteurMotsParCentroide[i]
            else:
                matriceCentroides[i]= np.zeros(self.nbMots)
                
        return matriceCentroides, vectCompteurMotsParCentroide
    
                 
    def comparerCentroideAvecMot(self,indexMot,centroide):
        return self.algo.leastSquares(indexMot, centroide)   
    
    def attribuerCentroidesAleatoirement(self):
        return np.random.randint(0, self.nbCentroides, size = self.nbMots)
    
    def transfererAuvectSuivant(self, vectSuivant):
        vect = np.copy(vectSuivant)
        vectSuivant = np.zeros(self.nbMots)
        return vect, vectSuivant
    
    def afficherResultatParIteration(self,iteration,vectCompteur,nbChangements):
        for i in range(len(vectCompteur)):
            self.afficherPointsParCentroide(vectCompteur[i],i)
        self.afficherEnteteIteration(iteration,nbChangements)
    
    def afficherVecteur(self, nomVecteur, vecteur, debut):
        print(" -- {}".format(nomVecteur))
        print(['{:.2f}'.format(i)for i in vecteur[debut:debut+50]])
        
    def afficherPointsParCentroide(self,points,centroide):
        print("Il y a {} points (mots) regroupés autour du centroïde # {}".format(points,centroide))
        
    def afficherEnteteIteration(self,no,nbChangementCluster):
        print("\n==============================")
        print("Iteration {} terminee. {} changement(s) de clusters.\n".format(no,str(int(nbChangementCluster))))
        
    def afficherNombreCentroideAleatoire(self,nb):
        print("{} centroïdes, générés aléatoirement.\n".format(nb))
        
    def afficherResultatsGroupe(self, vecteurAppartenance,matriceCentroides):
        dictInverse = {value :key for key,value in self.dictMotExistant.items()}
        print("Temps pour calculer les clusters : {}".format(time() - self.debut))
        matriceDistances = self.matriceAffichageMotProche(vecteurAppartenance,matriceCentroides)
        for i in range(self.nbCentroides):
            listeTuplesDistancesMinimales = self.trouverMotsPresCentroide(matriceDistances[i])
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("\nGroupe {}:\n".format(str(i)))
            for n in range(len(listeTuplesDistancesMinimales)):
                #for cle in sorted(self.dictMotExistant.keys()): 
                #if float(listeTuplesDistancesMinimales[n][0]) == self.dictMotExistant.get(cle):
                mot = dictInverse.get(listeTuplesDistancesMinimales[n][0])
                if listeTuplesDistancesMinimales[n][1] != sys.maxsize:
                    if self.estAnalyseVerbale:
                        if mot in self.dictionnaireVerbe:
                            print("{} ({}) -> {}".format(mot,self.dictionnaireVerbe[mot],listeTuplesDistancesMinimales[n][1]))
                    else:
                        print("{} -> {}".format(mot,listeTuplesDistancesMinimales[n][1]))
        
                        
    def matriceAffichageMotProche(self,vecteurAppartenance,matriceCentroides):  
              
        matriceAAfficher = np.zeros((self.nbCentroides, self.nbMots))
        
        for centroide in range(self.nbCentroides):
            vectIndexMotPourCeCentroide = np.zeros(self.nbMots)
            
            for i in range(len(vecteurAppartenance)):  
                if vecteurAppartenance[i] == centroide:
                    distance = self.algo.leastSquares(matriceCentroides[centroide], self.matriceCooccurrences[i])
                    vectIndexMotPourCeCentroide[i] = distance
                    
            for compteur in range(len(vectIndexMotPourCeCentroide)):

                matriceAAfficher[centroide][compteur] = vectIndexMotPourCeCentroide[compteur]
                
        return matriceAAfficher
    
    
    def trouverMotsPresCentroide(self, vecteurDistances):
        
        listeIndexSelectionnes = []
        
        for index in range(len(vecteurDistances)):
            if vecteurDistances[index]==0:
                vecteurDistances[index]=sys.maxsize

        for i in range(self.nombreMotsAAfficher):
            distance = np.amin(vecteurDistances)
            index = np.argmin(vecteurDistances)
            
            if (index,distance) not in listeIndexSelectionnes:
                listeIndexSelectionnes.append((index,distance))
                vecteurDistances[index] = sys.maxsize
                
        return listeIndexSelectionnes
    
    def genererDictionnaireVerbes(self):
        self.dictionnaireVerbe = {}
        with open("Lexique382.tsv") as f:
            contenu = csv.reader(f, delimiter="\t", quotechar='"')
            for ligne in contenu:
                if(ligne[3] == 'VER'):
                    self.dictionnaireVerbe[ligne[0]] = ligne[10]
            
    #def trouverVerbeInfos(self,mot):
    #    with open("Lexique382.tsv") as f:
    #        contenu = csv.reader(f, delimiter="\t", quotechar='"')
    #        for ligne in contenu:
    #            if(mot == ligne[0]):
    #                if(ligne[3] == 'VER'):
    #                    return ligne[10]
        
        
        