import sqlite3
from Constantes import Constantes as const

class DAO:
	def __init__(self):
		self.connexion = None
		self.cur = None
		
	def ouvrirConnexion(self):
		if self.connexion==None:
			self.connexion = sqlite3.connect("projetOracle.db")
		if self.cur == None:
			self.cur = self.connexion.cursor()
	
	def creerTable(self):
		self.ouvrirConnexion()
		
		self.cur.execute(const.REQUETE_CREATE_TABLE_MOTS)
		self.cur.execute(const.REQUETE_CREATE_TABLE_COOCURRENCES)
			
		self.fermerConnexion()


	def creerDictMotsExistants(self):
		self.ouvrirConnexion()
		self.cur.execute(const.REQUETE_SELECT_MOTS)
		mots = self.cur.fetchall()
		dictMots = {}
		for id, mot in mots:
			dictMots[mot] = id
		self.fermerConnexion()
		return dictMots
	
		self.ouvrirConnexion()
		dictCooccurencesDB = {}
		self.cur.execute(const.REQUETE_SELECT_COOCCURENCES)
		
		for mot1, mot2, taille, nb in self.cur.fetchall():
			dictCooccurencesDB[(mot1, mot2, taille)] = nb
		
		self.fermerConnexion()
		
		return dictCooccurencesDB
		
	def creerMatriceCooccurrences(self, tailleFenetre, matrice):
		self.ouvrirConnexion()
		
		requete = (const.REQUETE_SELECT_AVEC_TAILLEFENETRE)
		self.cur.execute(requete,{"t":tailleFenetre})
		
		for mot1, mot2, taille, nbCooccurrences in self.cur.fetchall():
			matrice[mot1][mot2] = nbCooccurrences	
			matrice[mot2][mot1] = matrice[mot1][mot2]	
		
		self.fermerConnexion()
		return matrice
	
	def creerDictCoocurrencesExistantes(self, tailleFenetre):
		self.ouvrirConnexion()
		dictCooccurrencesExistantes = {}
		requete = (const.REQUETE_SELECT_AVEC_TAILLEFENETRE)
		self.cur.execute(requete,{"t":tailleFenetre})
		for mot1, mot2, taille, nbCooccurrences in self.cur.fetchall():
			dictCooccurrencesExistantes[(mot1, mot2, taille)] = nbCooccurrences				
		
		self.fermerConnexion()
		return dictCooccurrencesExistantes
	
	
	def insertionsNouveauxMots(self, liste):
		self.ouvrirConnexion()
		self.cur.executemany(const.REQUETE_INSERT_MOTS_LISTE, liste)
		self.connexion.commit()
		self.fermerConnexion()
					
	def InsertionCooccurrences(self, listeInsertions):
		self.ouvrirConnexion()
		self.cur.executemany(const.REQUETE_INSERT_COOCCURRENCES, listeInsertions)
		self.connexion.commit()
		self.fermerConnexion()
		
	def UpdateCooccurrences(self, listeUpdate):
		self.ouvrirConnexion()
		self.cur.executemany(const.REQUETE_UPDATE_COOCCURRENCES, listeUpdate)
		self.connexion.commit()
		self.fermerConnexion()
	
	def trouverIndexMot(self,mot):
		self.ouvrirConnexion()
		self.cur.execute(const.REQUETE_SELECT_ID_MOTS,{'p':mot})
		
		resultat = self.cur.fetchall()
		
		if resultat == []:
			return -1
		else:
			for id in resultat:
				indexMot = id
		self.fermerConnexion()
		return indexMot[0]
	
	def fermerConnexion(self):
		self.cur.close()
		self.cur=None
		self.connexion.close()
		self.connexion=None
		
	
	def effacerTables(self):
		self.ouvrirConnexion()
		if self.siTableExiste("MOTS"):
			self.cur.execute(const.REQUETE_EFFACER_TABLE_MOTS)
		
		if self.siTableExiste("COOCCURRENCES"):
			self.cur.execute(const.REQUETE_EFFACER_TABLE_COOCCURRENCES)
			
		self.fermerConnexion()
			
		
