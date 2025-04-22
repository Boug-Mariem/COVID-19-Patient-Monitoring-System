import csv
#importation des class pour la gestion des personne
from biblio.class_personne import Personne
from biblio.class_dictionnaire_personne import DicPersonne

class Fichier_Personne():
    def __init__(self):
        self.chemifichier = "enregistrement/"
        self.nomfichier = "personne.csv"
        self.pointeurfichier = ""    
    
    def recuperation(self):         
        csv_chemin=self.chemifichier+self.nomfichier
        dicper=DicPersonne()
        with open(csv_chemin) as csv_file:
          self.pointeurfichier = csv.reader(csv_file, delimiter=';')  
          for row in self.pointeurfichier:
            cin=row[0]
            nom=row[1]
            prenom=row[2]
            tel=row[3]
            nat=row[4]
            age=row[5]
            dateIn=row[6]
            dec=row[7] 
            p=Personne(cin,nom,prenom,tel,nat,age,dateIn,dec)
            if(cin!="CIN"): 
                dicper.ajouter(p)
        return dicper

    def enregistrement(self, dicper):
        csv_chemin=self.chemifichier+self.nomfichier
        self.pointeurfichier=open(csv_chemin, 'w',newline='')
        writer = csv.writer(self.pointeurfichier, delimiter=';')          
        nbPersonne=dicper.nbpersonne()
        writer.writerow(['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE'])
        for i in range(nbPersonne):
            p=dicper.getPersonne(i)
            writer.writerow([p.cin,p.nom,p.prenom,p.tel,p.nationalite,p.age,p.dateinfection,p.decede])
        self.pointeurfichier.close()

          
