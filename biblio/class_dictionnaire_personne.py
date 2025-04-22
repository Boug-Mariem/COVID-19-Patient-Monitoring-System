from biblio.class_personne import Personne
import datetime

class DicPersonne:
    def __init__(self):
        self.listcin =[]
        self.listnom =[]
        self.listprenom =[]
        self.listtel = []
        self.listnationalite =[]
        self.listage =[]
        self.listdateinfection=[]
        self.listdecede =[]
        self.dic={"CIN":self.listcin,"NOM": self.listnom,"Prenom" :self.listprenom,"Tel": self.listtel,"Nationalite" :self.listnationalite,"Age" :self.listage,"Date_infection" :self.listdateinfection,"Decede":self.listdecede}
    
    def ajouter(self,p):
        self.listcin.append(p.cin)
        self.listnom.append(p.nom)
        self.listprenom.append(p.prenom)
        self.listtel.append(p.tel)
        self.listnationalite.append(p.nationalite)
        self.listage.append(p.age)
        self.listdateinfection.append(p.dateinfection)
        self.listdecede.append(p.decede)
    
    def supprimer(self,ind):
        self.listcin.pop(ind)
        self.listnom.pop(ind)
        self.listprenom.pop(ind)
        self.listtel.pop(ind)
        self.listnationalite.pop(ind)
        self.listage.pop(ind)
        self.listdateinfection.pop(ind)
        self.listdecede.pop(ind)
        
    def occurance(self,cin):
        if(len(self.listcin)!=0):
            return self.listcin.count(cin)
                
    
    def supprimercin(self,cin):
        if(self.listcin.count(cin)!=0):
            ind=self.listcin.index(cin)
            self.supprimer(ind)
    
    def supprimernationalite(self,nationalite):
        for i in range(len(self.listnationalite)):
            if(self.listnationalite[i]==nationalite):
                self.supprimer(i)

    def supprimerindicatif(self,indicatif):
        if(len(self.listtel)!=0):
            i=0
            while (i<len(self.listtel)):
                ch=self.listtel[i]
                chind=ch[:2]
                if(chind==indicatif):
                    self.supprimer(i)
                else:
                    i=i+1
    
    def recherchecin(self,cin):
        i=0
        while(i<len(self.listcin)  and cin!=self.listcin[i]):
            i=i+1
        if(i==len(self.listcin)):
            i=-1
            tel="-1"
        else:
            tel=self.listtel[i]
        return i,tel
    
    def modifiertel(self,indrech,teln):
        self.listtel[indrech]=str(teln)
    
    def modifierdec(self,inderech,dec):
        self.listdecede[inderech]=dec
    
    def recherchetel(self,tel):
        i=0
        while(i<len(self.listtel) and tel!=self.listtel[i]):
            i=i+1
        if(i==len(self.listtel)):
            i=-1
        return i
    
    def recherchenat(self,nat):
        i=0
        while(i<len(self.listnationalite) and nat!=self.listnationalite[i]  ):
            i=i+1
        if(i==len(self.listnationalite)):
            i=-1
        return i
    
    def rechercheindc(self,indc):
        if len(self.listtel)!=0:
            i=1
            ch=self.listtel[0]
            chind=ch[:2]
            if(indc==chind):
                return 0
            else:
                while(i<len(self.listtel) and indc!=chind ):
                    ch=self.listtel[i]
                    chind=ch[:2]
                    i=i+1
                return i
        else:
            return -1
        
    
    def getPersonne(self,indrech):
        p=Personne(self.listcin[indrech],self.listnom[indrech],self.listprenom[indrech],self.listtel[indrech],self.listnationalite[indrech],self.listage[indrech],self.listdateinfection[indrech],self.listdecede[indrech] )    
        return p
    
    def nbpersonne(self):
        return len(self.listnationalite)
    
    def dictionnairenat(self,nat):
        dicnat=DicPersonne()
        for i in range(len(self.listnationalite)):
            if(nat==self.listnationalite[i]):
                p=Personne(self.listcin[i],self.listnom[i],self.listprenom[i],self.listtel[i],self.listnationalite[i],self.listage[i],self.listdateinfection[i],self.listdecede[i])
                dicnat.ajouter(p)
        return dicnat
    
    def dictionnaireindc(self,indc):
        dicindc=DicPersonne()
        for i in range(len(self.listtel)):
            ch=self.listtel[i]
            chind=ch[:2]
            if(indc==chind):
                p=Personne(self.listcin[i],self.listnom[i],self.listprenom[i],self.listtel[i],self.listnationalite[i],self.listage[i],self.listdateinfection[i],self.listdecede[i])
                dicindc.ajouter(p)
        return dicindc
    
    def dictionnairedecede(self):
        dicdecede=DicPersonne()
        for i in range(len(self.listdecede)):
            if(self.listdecede[i]=="1"):
                p=Personne(self.listcin[i],self.listnom[i],self.listprenom[i],self.listtel[i],self.listnationalite[i],self.listage[i],self.listdateinfection[i],self.listdecede[i])
                dicdecede.ajouter(p)
        return dicdecede
    
    def dictionnairenondecede(self):
        dicnondecede=DicPersonne()
        for i in range(len(self.listdecede)):
            if(self.listdecede[i]=="0"):
                p=Personne(self.listcin[i],self.listnom[i],self.listprenom[i],self.listtel[i],self.listnationalite[i],self.listage[i],self.listdateinfection[i],self.listdecede[i])
                dicnondecede.ajouter(p)
        return dicnondecede
    

    def recherche_dates_avant_14_jours(self):
        aujourdhui = datetime.date.today()
        dicdate = DicPersonne()
        for i in range(len(self.listdateinfection)):
            try:
                date = datetime.datetime.strptime(self.listdateinfection[i], "%d/%m/%Y").date()
            except ValueError:
                continue
            x = aujourdhui - date
            if x.days <= 14:
                p = Personne(self.listcin[i], self.listnom[i], self.listprenom[i], self.listtel[i], self.listnationalite[i], self.listage[i], self.listdateinfection[i], self.listdecede[i])
                dicdate.ajouter(p)
        return dicdate
   
    def pourcentagedecede(self):
        if len(self.listdecede)!=0:
            nb_personnes= len(self.listdecede)
            nb_personnes_decede=0
            for i in range(len(self.listdecede)):
                if (self.listdecede[i]=="1"):
                    nb_personnes_decede=nb_personnes_decede+1        
            pourcentage = (nb_personnes_decede / nb_personnes) * 100 
            return round(pourcentage,3)
        
    def dictionnairerisque(self,dicmal):
        dicrisque=DicPersonne()
        if(len(self.listcin)!=0):
            for i in range(len(self.listcin)):
                if((int(self.listage[i])>=50 or dicmal.maladierisqe(self.listcin[i])) and int(self.listdecede[i])!="1" ):
                    p=Personne(self.listcin[i],self.listnom[i],self.listprenom[i],self.listtel[i],self.listnationalite[i],self.listage[i],self.listdateinfection[i],self.listdecede[i])
                    dicrisque.ajouter(p)
        return dicrisque

        
    def agenbannee(self,cin):
        for i in range(len(self.listcin)):
            if(cin==self.listcin[i]):
                return self.listage[i]      