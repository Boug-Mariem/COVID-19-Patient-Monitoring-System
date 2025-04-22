from biblio.class_maladie import Maladie
from biblio.class_dictionnaire_personne import DicPersonne
class DicMaladie:
    def __init__(self):
        self.listcode =[]
        self.listcin =[]
        self.listmaladie =[]
        self.listnombreannee = []

        self.dic={"CODE":self.listcode,"CIN": self.listcin,"MALADIE" :self.listmaladie,"NOMBRE D'ANNEE": self.listnombreannee}
    
    def ajouter(self,m):
        self.listcin.append(m.cin)
        self.listmaladie.append(m.maladie)
        self.listnombreannee.append(m.nombreannee)
        self.listcode.append(str(len(self.listcin)))
    def ajouter_2(self,m):
        self.listcin.append(m.cin)
        self.listmaladie.append(m.maladie)
        self.listnombreannee.append(m.nombreannee)
        self.listcode.append(m.code)
        
    
    def supprimer(self,ind):
        self.listcode.pop(ind)
        self.listcin.pop(ind)
        self.listmaladie.pop(ind)
        self.listnombreannee.pop(ind)
       

    def supprimermaladie(self,maladie):
        i = 0
        while i < len(self.listmaladie):
            if self.listmaladie[i] == maladie:
                self.supprimer(i)
            else:
                i += 1
        return i
    
                

    def recherchecinmaladie(self,cin,maladie):
        i = 0
        while (i < len(self.listcin)) and (cin != self.listcin[i] or maladie != self.listmaladie[i]):
            i += 1
        if i == len(self.listcin):
            i = -1
        return i


    def modifiernombreannee(self, i, nombreannee):
        #if (i >= 0 and i < len(self.listnombreannee)):
        self.listnombreannee[i] = str(nombreannee)
        
        
    def getMaladie(self,indrech):
        m=Maladie(self.listcode[indrech],self.listcin[indrech],self.listmaladie[indrech],self.listnombreannee[indrech])    
        return m

    
    def nbmaladie(self):
        return len(self.listmaladie)
    
    def recherchemaladie(self, maladie):
        i = 0
        while( (i < len(self.listmaladie)) and (maladie != self.listmaladie[i])):
            i += 1
        if i == len(self.listmaladie):
            i = -1
        return i
    
    def cin_list(self, maladie):
        cin_list = [] 
        for i in range(len(self.listmaladie)):
            if maladie == self.listmaladie[i]:
                cin_list.append(self.listcin[i]) 
        return cin_list 

    def afficher_noms_prenoms(self, dicper, cin_list):
        noms = []
        prenoms = []
        for cin in cin_list:
            index ,tel= dicper.recherchecin(cin)  
            if index != -1:
                nom = dicper.listnom[index]
                prenom = dicper.listprenom[index]
                noms.append(nom) 
                prenoms.append(prenom)
        return noms, prenoms
    
    def recherchecin(self, cin):
        i = 0
        while( (i < len(self.listcin)) and (cin != self.listcin[i])):
            i += 1
        if i == len(self.listcin):
            i = -1
        return i
    
    def dictionnairecin(self, cin):
        diccin = DicMaladie()
        for i in range(len(self.listcin)):
            if(cin==self.listcin[i]):
                m = Maladie(self.listcode[i], self.listcin[i], self.listmaladie[i], self.listnombreannee[i])
                diccin.ajouter_2(m)
        return diccin
    
    def pourcentageMaladie(self, maladie):
        if len(self.listcin)!=0:
            nb_personnes_total = len(self.listcin)
            nb_personnes_maladie = self.listmaladie.count(maladie)
            pourcentage = (nb_personnes_maladie / nb_personnes_total) * 100 
            return round(pourcentage,3)
    
    def maladierisqe(self,cin):
        if(self.listcin.count(cin)!=0):
            ind=self.listcin.index(cin)
            if(self.listmaladie[ind]=="DIABETE" or self.listmaladie[ind]=="HYPERTENSION" or self.listmaladie[ind]=="ASTHME"):
                return True

    def rechercheexiste(self,cin):
        i=0
        while(i<len(self.listcin) and self.listcin[i]!=cin ):
            i=i+1
        return i<len(self.listcin) 