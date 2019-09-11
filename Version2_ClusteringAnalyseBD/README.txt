/*********************************************
*					     *
* 	   Projet Oracle - Partie 3 	     *
*	      Jean-Simon Bondaz	     	     *
*	     Joé Bourgeois-Paquin	     *
*		  Claudia Roy		     *
*					     *
/*********************************************

==============================================
	     3 MODES D'UTILISATION
==============================================
Le présent projet se décline en 3 utilisations:

*****************Entrainement*****************
Exemple:

"-e"
	Active le mode entrainement

"-t [taille]"
	Définit la taille de la fenêtre de lecture

"--enc [encodage]" 
	Encodage de la ressource

"--chemin [chemin] [chemin] ..."
	Chemin relatif/absolu des fichiers sur 
	lesquels s'entrainer.

EXEMPLE : 
Y:\Cooccurrences\src> mainBD.py -e -t 5 --enc utf-8 --chemin textes\GerminalUTF8.txt

******************Recherche*******************

"-r"
	Active le mode recherche

"-t [taille]"
	Taille de la fenêtre voulue

EXEMPLE :
Y: \Cooccurrences\src>mainBD.py -r -t 5 


******************Clustering******************

"-c"
	Active le mode de clustering

"-t [taille]"
	Taille de la fenêtre pour les mots à analyser

"-n [nombre]"
	Nombre de mots et leur distance du centroïdes
	à afficher à la fin de l'algorithme.

"--nc [nombre]"
	Nombre de centroïdes à générer aléatoirement

==OPTIONNELS==
"-v"
	Active l'analyse verbale (montre seulement les verbes)
	CETTE OPTION N'AFFICHERA QUE LES VERBES À LA FIN
	DE L'AFFICHAGE (ou ce qui a la même graphie qu'un verbe)
 
EXEMPLE:
Y: \Cooccurrences\src>main.py -c -t 10 -n 10 --nc 25 > test\25c10t10a.txt