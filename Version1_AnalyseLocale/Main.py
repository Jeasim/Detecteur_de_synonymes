import sys
import Lecteur as lect
import Matrice as matr
import Affichage as aff
import Texte as txt
import Algorithmie as alg
import time

def main():

    try:
        lecteur = lect.Lecteur()
        affichage = aff.Affichage()
        langue = affichage.choixLangue()
        lecteur.definirLangue(langue)
        start = time.time()
        tailleFenetre = sys.argv[1]
        encodage = sys.argv[2]
        
        for parametre in range(3, len(sys.argv)):
            chemin = sys.argv[parametre]
            texte = txt.Texte(chemin, encodage, lecteur)
            lecteur.ajouterAuTableau(texte.tableauContenu)
            lecteur.remplirDictionnaire()
    
        texte = None
        matrice = matr.Matrice(tailleFenetre, lecteur.tableauDeMots, lecteur.dictionnaire)
        
        end = time.time()
        algo = alg.Algorithmie()
        
    except FileNotFoundError:
        affichage.erreurEncodage()   
        sys.exit()

    except LookupError:
        affichage.erreurChemin()
        sys.exit()
        
    except ValueError:
        affichage.erreurTailleFenetre()
        sys.exit()
                

    affichage.tempsEcoule("Entrainement",end-start)
    reponse = affichage.inputParamsRecherche()
    mot = reponse[0].casefold()

    
    while mot != 'q':
        
        if mot == 'l':
            langue = affichage.choixLangue()
            lecteur.definirLangue(langue)
        
        else:
            start = time.time()
            try:
                resultat = algo.calculresultats(reponse[2], matrice.matriceCooccurences, mot, lecteur)
                affichage.afficherResultats(int(reponse[1]) - 1, resultat, mot, lecteur.motStopList)
                end = time.time()
                affichage.tempsEcoule("Calcul",end-start)
                    
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

    affichage.finProgramme()   
   
  
if __name__ == '__main__':
    sys.exit(main())