import csv
#importation des class pour la gestion des maladies
from biblio.class_maladie import Maladie
from biblio.class_dictionnaire_maladie import DicMaladie

class Fichier_Maladie():
    def __init__(self):
        self.chemifichier = "enregistrement/"
        self.nomfichier = "maladie.csv"
        self.pointeurfichier = ""    
    
    def recuperation(self):         
        csv_chemin=self.chemifichier+self.nomfichier
        dicmal=DicMaladie()
        with open(csv_chemin) as csv_file:
          self.pointeurfichier = csv.reader(csv_file, delimiter=';')  
          for row in self.pointeurfichier:
            code=row[0]
            cin=row[1]
            maladie=row[2]
            nombreannee=row[3]
            m=Maladie(code,cin ,maladie ,nombreannee)
            if(cin!="CIN"):
                dicmal.ajouter(m)  
        return dicmal

    def enregistrement(self, dicmal):
        csv_chemin=self.chemifichier+self.nomfichier
        self.pointeurfichier=open(csv_chemin, 'w',newline='')
        writer = csv.writer(self.pointeurfichier, delimiter=';')          
        nbMaladie=dicmal.nbmaladie()
        writer.writerow(['CODE','CIN','MALADIE','NOMBRE D ANNEE'])
        for i in range(nbMaladie):
            m=dicmal.getMaladie(i)
            writer.writerow([m.code,m.cin ,m.maladie ,m.nombreannee])
        self.pointeurfichier.close()