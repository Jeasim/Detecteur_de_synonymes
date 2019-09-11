import re

class Lecteur:
    def __init__(self):
        self.langue = ""
        self.stopList = self.definirLangue(self.langue)
        self.tableauDeMots = []
        self.dictionnaire = {}  
      
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
                self.dictionnaire[self.tableauDeMots[i]] = compteur
                compteur += 1
            
    def definirLangue(self, langue):
        if langue == '0':
            self.langue = "français"
            self.stopList = ["lorsque","toute","ah","ainsi","car","chez","non","eux","venait","celui","au","aux","suis","oui","dont","bien","faire","y","avez","ai","j","m","cette","on","moi","me","c","a","plus","qu","dit","de","moi","n","avait","ne","se","était","s","lui","une","l","à","d","un","avait","alors", "au", "aucuns", "aussi", "autre", "avant", "avec", "avoir", "bon", "cas", "ce", "cela", "ces","ces","chaque","ci","comme","comment","dans","des","du","dedans","dehors","depuis","devrait","doit","donc","elle","elles","en","encore","est","et","eu","fait","faites","font","hors","ici","il","ils","je","juste","la","le","les","leur","là","ma","maintenant","mais","mes","mine","moins","mon","même","ni","notre","nous","ou","où","par","parce","pas","peut","peu","plupart","pour","pourquoi","quand","que","quel","quelle","quelles","quels","qui","sa","sans","ses","seulement","si","sien","son","sont","sous","soyez","sur","ta","tandis","tellement","tels","tes","ton","tous","tout","trop","très","tu","voient","vont","votre","vous","vu","ça","étaient","étions","été","être"]

        elif langue == '1':
            self.langue = "anglais"
            self.stopList = ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","like","me","more","most","mustn't","my","myself","no","nor","not","now","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she""she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","upon","very","was","wasn't","we","we'd","we'l","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]        
  
    
        
    def motStopList(self, mot):
        if mot in self.stopList:
            return 1
        else:
            return 0
