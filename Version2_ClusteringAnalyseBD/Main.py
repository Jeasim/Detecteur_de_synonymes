import sys
import Lecteur as lect
import Matrice as matr
import Affichage as aff
import Texte as txt
import DAO as dao
import Algorithmie as alg
import Dictionnaire as dict
import Clustering as cluster
from time import time
import getopt

def main():

    try:
        bd = dao.DAO()
        bd.creerTable()
        lecteur = lect.Lecteur()
        affichage = aff.Affichage()
        
        #c: clustering / n: nombre de mots à afficher par cluster / nc: nombre de centroïdes
        options, arguments = getopt.getopt(sys.argv[1:], 'erct:n:v', ['enc=','chemin=','nc=','mots='])
        
        entrainement = False
        recherche = False
        clustering = False
        analyseVerbale = False        
       
        for option, argument in options: 
            if option == '-e':
                entrainement = True   
                
            elif option == '-r':
                recherche = True
                
            elif option == '-c':
                clustering = True
                
            elif option == '-t':
                tailleFenetre = argument
                
            elif option == '-n':
                nombreMotsAffiches = argument
                
            elif option == '-v':
                analyseVerbale = True
                

        if entrainement:  
            affichage.entrainement()
            start = time()
            listeChemins = []
            
            for option, argument in options:  
                if option == '--enc':
                    encodage = argument
                    
                elif option == '--chemin':
                    listeChemins.append(argument)
            
            for chemin in listeChemins:        
                texte = txt.Texte(chemin, encodage, lecteur)
                lecteur.ajouterAuTableau(texte.tableauContenu)
                lecteur.remplirDictionnaire()
                
                    
            bd.insertionsNouveauxMots(lecteur.listeNouveauxMotsBD)
                    
            dictCooccurrences = dict.Dictionnaire(tailleFenetre, lecteur.tableauDeMots, lecteur.dictionnaire)
            dictionnaireCooccurences = dictCooccurrences.construireDictionnaireCooccurences()
            dictionnaireCooccurrencesExistantes = bd.creerDictCoocurrencesExistantes(tailleFenetre)
            tupleListes = lecteur.trierInsertUpdate(dictionnaireCooccurrencesExistantes, dictionnaireCooccurences)
            
            bd.InsertionCooccurrences(tupleListes[0])
            bd.UpdateCooccurrences(tupleListes[1])
            
         
            affichage.tempsEcoule("Entrainement",time()-start)
            
            
        texte = None
                

    except FileNotFoundError:
        affichage.erreurChemin()
        sys.exit()
        
    except LookupError:
        affichage.erreurEncodage()   
        sys.exit()
        
    except ValueError:
        affichage.erreurTailleFenetre()
        sys.exit()
        
    except getopt.GetoptError:
        affichage.erreurArgumentLigneDeCommande()
        sys.exit()        
   
    if recherche:
        affichage.recherche()
        start = time()
        algo = alg.Algorithmie()
        matrice = matr.Matrice(lecteur.dictMotsDB)
        matriceCooccurrences = bd.creerMatriceCooccurrences(tailleFenetre, matrice.matriceVide)
        affichage.tempsEcoule("Initialisation de la recherche ",time()-start)
        reponse = affichage.inputParamsRecherche()
        mot = reponse[0].casefold()
        
        while mot != 'q':

            try:
                indexMot = bd.trouverIndexMot(mot)
                
                #Mot qui n'existe pas
                if indexMot == -1:
                    raise KeyError()
                
                
                resultat = algo.calculresultats(reponse[2], indexMot,mot, matriceCooccurrences, lecteur.dictMotsDB)
                affichage.afficherResultats(int(reponse[1]) - 1, resultat, mot, lecteur.motStopList)
               
                    
            except KeyError:
                affichage.erreurMotInexistant()
            
            except UnboundLocalError:
                affichage.erreurChoixAlgo()
    
            except ValueError:
                affichage.erreurNombreSynonymes()
                
            except IndexError:
                affichage.erreurNombreParametresRecherche()
                    
            reponse = affichage.inputParamsRecherche()
            mot = reponse[0].casefold()
    
    try:
        if clustering:
            nbCentroides = 0
            listeIndexMots = []
            for option, argument in options:
                if option == '--nc':
                    nbCentroides = int(argument)
                elif option == '--mots':
                    listeMots = argument

                    for mot in listeMots.split():
                        indexMot = bd.trouverIndexMot(mot)
                
                        if indexMot == -1:
                            raise KeyError()
                        else:
                            listeIndexMots.append(indexMot)
                            
            algo = alg.Algorithmie()
            matrice = matr.Matrice(lecteur.dictMotsDB)
            matriceCooccurrences = bd.creerMatriceCooccurrences(tailleFenetre, matrice.matriceVide)
            objClustering = cluster.Clustering(matriceCooccurrences, listeIndexMots, nombreMotsAffiches, nbCentroides,analyseVerbale)
            objClustering.bouclePrincipale()
            
    except ValueError:
        affichage.erreurTailleFenetre()
        sys.exit()
        
    except KeyError:
        affichage.erreurMotInexistant()

    affichage.finProgramme()   
   
  
if __name__ == '__main__':
    sys.exit(main())