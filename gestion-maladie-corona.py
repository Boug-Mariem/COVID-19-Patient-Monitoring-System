from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QMessageBox

from biblio.main import Ui_MainWindow 

from biblio.ajouterpersonne import Ui_Dialog as ajouterpersonneDialog
from biblio.ajoutermaladie import Ui_Dialog as ajoutermaladieDialog
from biblio.supprimercin import Ui_Dialog as supprimercinDialog
from biblio.supprimernationalite import Ui_Dialog as supprimernationaliteDialog
from biblio.supprimertelephone import Ui_Dialog as supprimertelephoneDialog
from biblio.supprimermaladie import Ui_Dialog as supprimermaladieDialog
from biblio.modifiernumpers import Ui_Dialog as modifiernumpersDialog
from biblio.modifierdecespers import Ui_Dialog as modifierdecespersDialog
from biblio.modifiernbmaladie import Ui_Dialog as modifiernbmaladieDialog

from biblio.affichagemaladieschaquepersonne import Ui_Form as affichagemaladieschaquepersonneForm
from biblio.affichagemaladiespersonne import Ui_Form as affichagemaladiespersonneForm
from biblio.affichageparindicatif import Ui_Form as affichageparindicatifForm
from biblio.affichageparmaladies import Ui_Form as affichageparmaladiesForm
from biblio.affichageparnationalite import Ui_Form as affichageparnationaliteForm
from biblio.affichagepartelephone import Ui_Form as affichagepartelephoneForm
from biblio.affichagepersonnedecedes import Ui_Form as affichagepersonnedecedesForm
from biblio.affichagepersonnenondecedes import Ui_Form as affichagepersonnenondecedesForm
from biblio.affichagetouspersonne import Ui_Form as affichagetouspersonneForm
from biblio.affichagetoutesmaladies import Ui_Form as affichagetoutesmaladiesForm
from biblio.recherchepourcentagechaquemaladie import Ui_Form as recherchepourcentagechaquemaladieForm
#vrif
from biblio.calculetaffichage import Ui_Form as calculetaffichageForm

from biblio.calculetaffichageparnationalite import Ui_Form as calculetaffichageparnationaliteForm
from biblio.calculetaffichagepersonnearisque import Ui_Form as calculetaffichagepersonnearisqueForm
from biblio.calculetaffichagepersonnedecedes import Ui_Form as calculetaffichagepersonnedecedesForm
from biblio.calculetaffichagepersonneenquarantaine import Ui_Form as calculetaffichagepersonneenquarantaineForm
#importation des class pour la gestion des personne
from biblio.class_personne import Personne
from biblio.class_dictionnaire_personne import DicPersonne
#importation des class pour la gestion des maladies
from biblio.class_maladie import Maladie
from biblio.class_dictionnaire_maladie import DicMaladie
#importation des class pour gestion des fichier 
from biblio.class_fichier_personne import Fichier_Personne
from biblio.class_fichier_maladie import Fichier_Maladie

import datetime

import sys


def afficheajouterpersonne():
    if (recpper==True):
        ajouterpersonne.exec_()
    else:
        QMessageBox.critical(None, "Erreur", "Veuillez récupérer les données des personnes avant d'ajouter \n")

def afficheajoutermaladie():
    if (recpmal==True):
        ajoutermaladie.exec_()
    else:
        QMessageBox.critical(None, "Erreur", "Veuillez récupérer les données des maladies avant d'ajouter \n")
def affichesupprimercin():
    supprimercin.exec_()
def affichesupprimertelephone():
    supprimertelephone.exec_()
def affichesupprimernationalite():
    supprimernationalite.exec_()
def affichesupprimermaladie():
    supprimermaladie.exec_()
def affichemodifiernumpers():
    modifiernumpers.exec_()    
def affichemodifierdecespers():
    modifierdecespers.exec_()
    
def affichemodifiernbmaladie():
    modifiernbmaladie.exec_()

def afficheaffichagemaladieschaquepersonne():
    L=0
    for i in range (len(dicper.listcin)):
        ind=dicmal.recherchecin(dicper.listcin[i])
        if (ind!=-1):
            dicpm= dicmal.dictionnairecin(dicper.listcin[i])
            nbm=dicpm.nbmaladie()
            
            tableauaffichagemaladieschaquepersonne=uiaffichagemaladieschaquepersonne.getTable()
            headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE','CODE','MALADIE','NOMBRE D ANNEE']
            nbMaladie=dicmal.nbmaladie()
            tableauaffichagemaladieschaquepersonne.setRowCount(nbMaladie)
            tableauaffichagemaladieschaquepersonne.setColumnCount(11)
            tableauaffichagemaladieschaquepersonne.setHorizontalHeaderLabels(headerH)
            headersize=tableauaffichagemaladieschaquepersonne.horizontalHeader()
            headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(8, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(9, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(10, QHeaderView.ResizeToContents)
        
            p=dicper.getPersonne(i)
            tableauaffichagemaladieschaquepersonne.setItem(L , 0 , QTableWidgetItem(p.cin))
            tableauaffichagemaladieschaquepersonne.setItem(L , 1 , QTableWidgetItem(p.nom))
            tableauaffichagemaladieschaquepersonne.setItem(L , 2 , QTableWidgetItem(p.prenom))
            tableauaffichagemaladieschaquepersonne.setItem(L , 3 , QTableWidgetItem(p.tel))
            tableauaffichagemaladieschaquepersonne.setItem(L , 4 , QTableWidgetItem(p.nationalite))
            tableauaffichagemaladieschaquepersonne.setItem(L , 5 , QTableWidgetItem(p.age))
            tableauaffichagemaladieschaquepersonne.setItem(L , 6 , QTableWidgetItem(p.dateinfection))
            tableauaffichagemaladieschaquepersonne.setItem(L , 7 , QTableWidgetItem(p.decede))
            
            for j in range(nbm):
                m=dicpm.getMaladie(j)
                tableauaffichagemaladieschaquepersonne.setItem(L , 8 , QTableWidgetItem(m.code))
                tableauaffichagemaladieschaquepersonne.setItem(L , 9 , QTableWidgetItem(m.maladie))
                tableauaffichagemaladieschaquepersonne.setItem(L , 10 , QTableWidgetItem(m.nombreannee))
                L=L+1
    
    affichagemaladieschaquepersonne.exec_()
    
    
    
def afficheaffichagemaladiespersonne():
    affichagemaladiespersonne.exec_()
def afficheaffichageparindicatif():
    affichageparindicatif.exec_()
def afficheaffichageparmaladies():
    affichageparmaladies.exec_()
def afficheaffichageparnationalite():
    affichageparnationalite.exec_()
def affichageaffichagepartelephone():
    affichagepartelephone.exec_()
def afficheaffichagepersonnedecedes():
    dicdecede=dicper.dictionnairedecede()
    nbpersonne=dicdecede.nbpersonne()
    
    tableaffichedecede=uiaffichagepersonnedecedes.getTable()
    headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
    nbPersonne=dicdecede.nbpersonne()
    tableaffichedecede.setRowCount(nbPersonne)
    tableaffichedecede.setColumnCount(8)
    tableaffichedecede.setHorizontalHeaderLabels(headerH)
    headersize=tableaffichedecede.horizontalHeader()
    headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
    if (nbpersonne!=0):    
        for i in range(nbPersonne):
            p=dicdecede.getPersonne(i)
            tableaffichedecede.setItem(i , 0 , QTableWidgetItem(p.cin))
            tableaffichedecede.setItem(i , 1 , QTableWidgetItem(p.nom))
            tableaffichedecede.setItem(i , 2 , QTableWidgetItem(p.prenom))
            tableaffichedecede.setItem(i , 3 , QTableWidgetItem(p.tel))
            tableaffichedecede.setItem(i , 4 , QTableWidgetItem(p.nationalite))
            tableaffichedecede.setItem(i , 5 , QTableWidgetItem(p.age))
            tableaffichedecede.setItem(i , 6 , QTableWidgetItem(p.dateinfection))
            tableaffichedecede.setItem(i , 7 , QTableWidgetItem(p.decede))
    
    affichagepersonnedecedes.exec_()
def afficheaffichagepersonnenondecedes():
    dicnondecede=dicper.dictionnairenondecede()
    tableaffichenondecede=uiaffichagepersonnenondecedes.getTable()
    headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
    nbPersonne=dicnondecede.nbpersonne()
    tableaffichenondecede.setRowCount(nbPersonne)
    tableaffichenondecede.setColumnCount(8)
    tableaffichenondecede.setHorizontalHeaderLabels(headerH)
    headersize=tableaffichenondecede.horizontalHeader()
    headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
    for i in range(nbPersonne):
        p=dicnondecede.getPersonne(i)
        tableaffichenondecede.setItem(i , 0 , QTableWidgetItem(p.cin))
        tableaffichenondecede.setItem(i , 1 , QTableWidgetItem(p.nom))
        tableaffichenondecede.setItem(i , 2 , QTableWidgetItem(p.prenom))
        tableaffichenondecede.setItem(i , 3 , QTableWidgetItem(p.tel))
        tableaffichenondecede.setItem(i , 4 , QTableWidgetItem(p.nationalite))
        tableaffichenondecede.setItem(i , 5 , QTableWidgetItem(p.age))
        tableaffichenondecede.setItem(i , 6 , QTableWidgetItem(p.dateinfection))
        tableaffichenondecede.setItem(i , 7 , QTableWidgetItem(p.decede))
    
    affichagepersonnenondecedes.exec_()
def afficheaffichagetouspersonne():
    tableauaffichatouspersonne=uiaffichagetouspersonne.getTable()
    headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
    nbPersonne=dicper.nbpersonne()
    tableauaffichatouspersonne.setRowCount(nbPersonne)
    tableauaffichatouspersonne.setColumnCount(8)
    tableauaffichatouspersonne.setHorizontalHeaderLabels(headerH)
    headersize=tableauaffichatouspersonne.horizontalHeader()
    headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
    for i in range(nbPersonne):
        p=dicper.getPersonne(i)
        tableauaffichatouspersonne.setItem(i , 0 , QTableWidgetItem(p.cin))
        tableauaffichatouspersonne.setItem(i , 1 , QTableWidgetItem(p.nom))
        tableauaffichatouspersonne.setItem(i , 2 , QTableWidgetItem(p.prenom))
        tableauaffichatouspersonne.setItem(i , 3 , QTableWidgetItem(p.tel))
        tableauaffichatouspersonne.setItem(i , 4 , QTableWidgetItem(p.nationalite))
        tableauaffichatouspersonne.setItem(i , 5 , QTableWidgetItem(p.age))
        tableauaffichatouspersonne.setItem(i , 6 , QTableWidgetItem(p.dateinfection))
        tableauaffichatouspersonne.setItem(i , 7 , QTableWidgetItem(p.decede))
    
    affichagetouspersonne.exec_()
def afficheaffichagetoutesmaladies():
    tableauaffichagetoutesmaladies=uiaffichagetoutesmaladies.getTable()
    headerH = ['CODE','CIN','MALADIE','NOMBRE D ANNEE']
    nbMaladie=dicmal.nbmaladie()
    tableauaffichagetoutesmaladies.setRowCount(nbMaladie)
    tableauaffichagetoutesmaladies.setColumnCount(4)
    tableauaffichagetoutesmaladies.setHorizontalHeaderLabels(headerH)
    headersize=tableauaffichagetoutesmaladies.horizontalHeader()
    """headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)"""
    headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    
    for i in range(nbMaladie):
        m=dicmal.getMaladie(i)
        tableauaffichagetoutesmaladies.setItem(i , 0 , QTableWidgetItem(m.code))
        tableauaffichagetoutesmaladies.setItem(i , 1 , QTableWidgetItem(m.cin))
        tableauaffichagetoutesmaladies.setItem(i , 2 , QTableWidgetItem(m.maladie))
        tableauaffichagetoutesmaladies.setItem(i , 3 , QTableWidgetItem(m.nombreannee))
       
    affichagetoutesmaladies.exec_()
    
def afficherecherchepourcentagechaquemaladie():
    recherchepourcentagechaquemaladie.exec_()
    
#verif
def affichecalculetaffichage():
    calculetaffichage.exec_()

def affichecalculetaffichageparnationalite():
    calculetaffichageparnationalite.exec_()
def affichecalculetaffichagepersonnearisque():
    dicrisque=dicper.dictionnairerisque(dicmal)
    nbpersonne=dicrisque.nbpersonne()
    tableafficherisque=ui2calculetaffichagepersonnearisque.getTable()
    headerH = ['NON','PRENOM','POURENTAGE']
    tableafficherisque.setRowCount(nbpersonne)
    tableafficherisque.setColumnCount(3)
    tableafficherisque.setHorizontalHeaderLabels(headerH)
    headersize=tableafficherisque.horizontalHeader()
    headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    if(nbpersonne!=0):
        for i in range(nbpersonne):
            pourcentage=0
            indp=dicper.listcin.index(dicrisque.listcin[i])
            if(dicmal.rechercheexiste(dicrisque.listcin[i])):
                indm=dicmal.listcin.index(dicrisque.listcin[i])
                if(dicmal.listmaladie[indm]=="DIABETE"):
                    pourcentage=pourcentage+15
                if(dicmal.listmaladie[indm]=="HYPERTENSION"):
                    pourcentage=pourcentage+20
                if(dicmal.listmaladie[indm]=="ASTHME"):
                   pourcentage=pourcentage+20
            if(int(dicper.listage[indp])>70):
                pourcentage=pourcentage+20
            if(70>=int(dicper.listage[indp])>=50):
                pourcentage=pourcentage+10
            
            chpourcentage=str(pourcentage)+' %'
            tableafficherisque.setItem(i , 0 , QTableWidgetItem(dicper.listnom[indp]))
            tableafficherisque.setItem(i , 1 , QTableWidgetItem(dicper.listprenom[indp]))
            tableafficherisque.setItem(i , 2 , QTableWidgetItem(chpourcentage))
            
    calculetaffichagepersonnearisque.exec_()
def affichecalculetaffichagepersonnedecedes():
    dicdecede=dicper.dictionnairedecede()
    nbpersonne=dicdecede.nbpersonne()
    if (nbpersonne!=0):
        tableaffichedecede=ui2calculetaffichagepersonnedecedes.getTable()
        headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
        nbPersonne=dicdecede.nbpersonne()
        tableaffichedecede.setRowCount(nbPersonne)
        tableaffichedecede.setColumnCount(8)
        tableaffichedecede.setHorizontalHeaderLabels(headerH)
        headersize=tableaffichedecede.horizontalHeader()
        headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        for i in range(nbPersonne):
            p=dicdecede.getPersonne(i)
            tableaffichedecede.setItem(i , 0 , QTableWidgetItem(p.cin))
            tableaffichedecede.setItem(i , 1 , QTableWidgetItem(p.nom))
            tableaffichedecede.setItem(i , 2 , QTableWidgetItem(p.prenom))
            tableaffichedecede.setItem(i , 3 , QTableWidgetItem(p.tel))
            tableaffichedecede.setItem(i , 4 , QTableWidgetItem(p.nationalite))
            tableaffichedecede.setItem(i , 5 , QTableWidgetItem(p.age))
            tableaffichedecede.setItem(i , 6 , QTableWidgetItem(p.dateinfection))
            tableaffichedecede.setItem(i , 7 , QTableWidgetItem(p.decede))
    
    pourcentage = dicper.pourcentagedecede()
    ui2calculetaffichagepersonnedecedes.lineEdit.setText(str(pourcentage)+' %')
    
    calculetaffichagepersonnedecedes.exec_()
    
def affichecalculetaffichagepersonneenquarantaine():
    dicdate=dicper.recherche_dates_avant_14_jours()
    tableaucalculetaffichagepersonneenquarantaine=ui2calculetaffichagepersonneenquarantaine.getTable()
    headerH = ['CIN','NON','PRENOM',"DATE D'INFECTION"]
    nbPersonne=dicdate.nbpersonne()
    tableaucalculetaffichagepersonneenquarantaine.setRowCount(nbPersonne)
    tableaucalculetaffichagepersonneenquarantaine.setColumnCount(4)
    tableaucalculetaffichagepersonneenquarantaine.setHorizontalHeaderLabels(headerH)
    headersize=tableaucalculetaffichagepersonneenquarantaine.horizontalHeader()
    headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    
    for i in range(nbPersonne):
         p=dicdate.getPersonne(i)
         tableaucalculetaffichagepersonneenquarantaine.setItem(i , 0 , QTableWidgetItem(p.cin))
         tableaucalculetaffichagepersonneenquarantaine.setItem(i , 1 , QTableWidgetItem(p.nom))
         tableaucalculetaffichagepersonneenquarantaine.setItem(i , 2 , QTableWidgetItem(p.prenom))
         tableaucalculetaffichagepersonneenquarantaine.setItem(i , 3 , QTableWidgetItem(p.dateinfection))
    
    calculetaffichagepersonneenquarantaine.exec_()
    
#gestion des fichier
recpper=False
recpmal=False
def enregistrer_fichier_personne():
    if (recpper==True):
        fper=Fichier_Personne()
        fper.enregistrement(dicper)
        QMessageBox.information(None, "Validation", "L'enregistremenet a été effectuée avec succès")
    else:
        QMessageBox.critical(None, "Erreur", "Veuillez récupérer les données des personnes avant\n")
    
def recuperer_fichier_personne():
    fper=Fichier_Personne()
    global dicper
    dicper=fper.recuperation()
    QMessageBox.information(None, "Validation", "La recuperation a été effectuée avec succès")
    global recpper
    recpper=True
def enregistrer_fichier_maladie():
    if(recpmal==True):
        fmal=Fichier_Maladie()
        fmal.enregistrement(dicmal)
        QMessageBox.information(None, "Validation", "L'enregistremenet a été effectuée avec succès")
    else:
        QMessageBox.critical(None, "Erreur", "Veuillez récupérer les données des maladies avant\n")
def recuperer_fichier_maladie():
    fmal=Fichier_Maladie()
    global dicmal
    dicmal=fmal.recuperation()
    QMessageBox.information(None, "Validation", "La recuperation a été effectuée avec succès")
    global recpmal
    recpmal=True
###########################################programme gestion des personne############################################################################
dicper=DicPersonne()
#ajouter_personne
def fajouterpersonne():
    cin = uiajouterpersonne.lineEdit.text()
    nom = uiajouterpersonne.lineEdit_2.text()
    prenom = uiajouterpersonne.lineEdit_9.text()
    tel = uiajouterpersonne.lineEdit_10.text()
    nationalite = uiajouterpersonne.lineEdit_7.text()
    age = uiajouterpersonne.lineEdit_3.text()
    dateinfection=uiajouterpersonne.dateEdit.text()
    decede = uiajouterpersonne.comboBox.currentText()    
    aujourdhui=datetime.date.today()
    date=datetime.datetime.strptime(dateinfection,"%d/%m/%Y").date()
    date_debut_corona=datetime.datetime.strptime("16/11/2019", "%d/%m/%Y").date()
    #les conditions d'ajout
    message_erreur=""
    if len(cin)!=8 or cin.isdigit()==False or dicper.occurance(cin)==1:
        message_erreur=message_erreur+"Veuillez vérifier le numéro de CIN saisie\n"
    if len(nom)<3 or nom.isalpha()==False :
        message_erreur=message_erreur+"Veuillez vérifier le nom saisie\n"
    if len(prenom)<3 or prenom.isalpha()==False :
        message_erreur=message_erreur+"Veuillez vérifier le prenom saisie\n"
    if len(tel)!=8 or tel.isdigit()==False :
        message_erreur=message_erreur+"Veuillez vérifier le numero de téléphone saisie\n"
    if age.isdigit()==False :
        message_erreur=message_erreur+"Veuillez vérifier l'age saisie\n"
    if len(nationalite)<3 or nationalite.isalpha()==False :
        message_erreur=message_erreur+"Veuillez vérifier la nationalité saisie\n"
    elif nationalite.isdigit()==False and nationalite.isupper()==False:
        message_erreur=message_erreur+"Veuillez Resaisir la nationalité en MAJUSCULE\n"      
    if ((aujourdhui-date>aujourdhui-date_debut_corona) or ((aujourdhui-date).days>int(age)*365)):
        message_erreur=message_erreur+"Veuillez vérifier la date d'infection\n"
    if message_erreur=="":
        p=Personne(cin,nom,prenom,tel,nationalite,age,dateinfection,decede)
        dicper.ajouter(p)
        QMessageBox.information(None, "Validation", "Ajout avec succès")
        uiajouterpersonne.reset_fields()
        QApplication.activeWindow().close()
    else :
        QMessageBox.critical(None, "Erreur", message_erreur)

#supprimer par cin
def fsupprimercin():
    cin=uisupprimercin.lineEdit.text()
    i,tel=dicper.recherchecin(cin)
    #les conditions de suppression
    if len(cin)!=8 or cin.isdigit()==False or i==-1 :
        QMessageBox.critical(None, "Erreur","Veuillez vérifier le numéro de CIN saisie\n")
    else :
        dicper.supprimercin(cin)
        QMessageBox.information(None, "Validation", "Supprimé avec succès !")
        uisupprimercin.reset_fields()
        QApplication.activeWindow().close()
        
#supprimer par nationalite
def fsupprimernationalite():
    nationalite=uisupprimernationalite.lineEdit.text()
    i=dicper.recherchenat(nationalite)
    #les conditions de suppression
    if len(nationalite)<3 or nationalite.isalpha()==False :
        QMessageBox.critical(None, "Erreur","Veuillez vérifier que la nationalité saisie")
    else :
        dicper.supprimernationalite(nationalite)
        QMessageBox.information(None, "Validation", "Supprimé avec succès !")
        uisupprimernationalite.reset_fields()
        QApplication.activeWindow().close()

#supprimer par indicatif
def fsupprimerindicatif():
    indicatif=uisupprimertelephone.lineEdit.text()   
    #les conditions de suppression
    if len(indicatif)!=2 or indicatif.isdigit()==False :
        QMessageBox.critical(None, "Erreur","Veuillez vérifier l'indicatif saisie\n")
    else :
        dicper.supprimerindicatif(indicatif)
        QMessageBox.information(None, "Validation","Supprimé avec succès !")
        uisupprimertelephone.reset_fields()
        QApplication.activeWindow().close()

#modifier le num avec recherche cin
indrech=-1
def frecherchecin():
    cin=uimodifiernumpers.lineEdit.text()
    global indrech
    indrech,tel=dicper.recherchecin(cin)
    if(indrech==-1): 
        QMessageBox.critical(None, "Erreur", "Veuillez vérifier le numéro de CIN saisie\n")
    else:
        uimodifiernumpers.lineEdit_2.setText(tel)
def frecherchecindece():
    cin=uimodifierdecespers.lineEdit.text()
    global indrech
    indrech,tel=dicper.recherchecin(cin)
    if(indrech==-1): 
        QMessageBox.critical(None, "Erreur", "Veuillez vérifier le numéro de CIN saisie\n")

def fmodifiernumpers():
    teln=uimodifiernumpers.lineEdit_2.text()
    if len(teln)!=8 or teln.isdigit()==False :
        QMessageBox.critical(None, "Erreur","Veuillez vérifier le numéro de téléphone saisie\n")
    else:
        dicper.modifiertel(indrech,teln)
        QMessageBox.information(None, "Validation", "La modification a été effectuée avec succès")
        uimodifiernumpers.reset_fields()
        QApplication.activeWindow().close()

#modifier le dece avec recherche cin
def fmodifierdece():
    dec=uimodifierdecespers.comboBox.currentText() 
    dicper.modifierdec(indrech,dec)
    QMessageBox.information(None, "Validation", "La modification a été effectuée avec succès")
    uimodifierdecespers.reset_fields()
    QApplication.activeWindow().close()
    
#affichage par numero de telephone    
def frechercheaffichetel():
    tel=uiaffichagepartelephone.linetel.text()
    indrech=dicper.recherchetel(tel)
    if(indrech==-1):
        QMessageBox.critical(None, "Erreur","Veuillez vérifier le numéro de téléphone saisie\n")
    else:
        tableaffichepartel=uiaffichagepartelephone.getTable()
        headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
        tableaffichepartel.setRowCount(1)
        tableaffichepartel.setColumnCount(8)
        tableaffichepartel.setHorizontalHeaderLabels(headerH)
        headersize=tableaffichepartel.horizontalHeader()
        headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        p=dicper.getPersonne(indrech)
        tableaffichepartel.setItem(0 , 0 , QTableWidgetItem(p.cin))
        tableaffichepartel.setItem(0 , 1 , QTableWidgetItem(p.nom))
        tableaffichepartel.setItem(0 , 2 , QTableWidgetItem(p.prenom))
        tableaffichepartel.setItem(0 , 3 , QTableWidgetItem(p.tel))
        tableaffichepartel.setItem(0 , 4 , QTableWidgetItem(p.nationalite))
        tableaffichepartel.setItem(0 , 5 , QTableWidgetItem(p.age))
        tableaffichepartel.setItem(0 , 6 , QTableWidgetItem(p.dateinfection))
        tableaffichepartel.setItem(0 , 7 , QTableWidgetItem(p.decede))
        
#affiche par nationalite
def frechercheaffichenat():
    nat=uiaffichageparnationalite.lineEdit.text()
    indrech=dicper.recherchenat(nat)
    if(indrech==-1):
        QMessageBox.critical(None, "Erreur","Veuillez vérifier que la nationalité saisie\n")
    else:
        dicnat=dicper.dictionnairenat(nat)
        tableafficheparnat=uiaffichageparnationalite.getTable()
        headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
        nbPersonne=dicnat.nbpersonne()
        tableafficheparnat.setRowCount(nbPersonne)
        tableafficheparnat.setColumnCount(8)
        tableafficheparnat.setHorizontalHeaderLabels(headerH)
        headersize=tableafficheparnat.horizontalHeader()
        headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        for i in range(nbPersonne):
            p=dicnat.getPersonne(i)
            tableafficheparnat.setItem(i , 0 , QTableWidgetItem(p.cin))
            tableafficheparnat.setItem(i , 1 , QTableWidgetItem(p.nom))
            tableafficheparnat.setItem(i , 2 , QTableWidgetItem(p.prenom))
            tableafficheparnat.setItem(i , 3 , QTableWidgetItem(p.tel))
            tableafficheparnat.setItem(i , 4 , QTableWidgetItem(p.nationalite))
            tableafficheparnat.setItem(i , 5 , QTableWidgetItem(p.age))
            tableafficheparnat.setItem(i , 6 , QTableWidgetItem(p.dateinfection))
            tableafficheparnat.setItem(i , 7 , QTableWidgetItem(p.decede))
            
#affiche par indicatif
def frechercheafficheindc():
    indc=uiaffichageparindicatif.lineEdit.text()
    indrech=dicper.rechercheindc(indc)
    if(indrech==-1):
        QMessageBox.critical(None, "Erreur","Veuillez vérifier l'indicatif saisie\n")
    elif(len(indc)!=2):
        QMessageBox.critical(None, "Erreur","Veuillez entrer 2 chiffres\n")
    else:
        dicindc=dicper.dictionnaireindc(indc)
        tableafficheparindc=uiaffichageparindicatif.getTable()
        headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE']
        nbPersonne=dicindc.nbpersonne()
        tableafficheparindc.setRowCount(nbPersonne)
        tableafficheparindc.setColumnCount(8)
        tableafficheparindc.setHorizontalHeaderLabels(headerH)
        headersize=tableafficheparindc.horizontalHeader()
        headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        for i in range(nbPersonne):
            p=dicindc.getPersonne(i)
            tableafficheparindc.setItem(i , 0 , QTableWidgetItem(p.cin))
            tableafficheparindc.setItem(i , 1 , QTableWidgetItem(p.nom))
            tableafficheparindc.setItem(i , 2 , QTableWidgetItem(p.prenom))
            tableafficheparindc.setItem(i , 3 , QTableWidgetItem(p.tel))
            tableafficheparindc.setItem(i , 4 , QTableWidgetItem(p.nationalite))
            tableafficheparindc.setItem(i , 5 , QTableWidgetItem(p.age))
            tableafficheparindc.setItem(i , 6 , QTableWidgetItem(p.dateinfection))
            tableafficheparindc.setItem(i , 7 , QTableWidgetItem(p.decede))

            
#####################################################################################################################################################

###########################################programme gestion des maladies############################################################################
dicmal=DicMaladie()
def fajoutermaladie():
    #code = uiajoutermaladie.lineEdit.text()
    cin = uiajoutermaladie.lineEdit_2.text()
    maladie = uiajoutermaladie.comboBox.currentText() 
    nombreannee = uiajoutermaladie.lineEdit_10.text()
    indrech,tel=dicper.recherchecin(cin)
    age=dicper.agenbannee(cin)
    #les conditions d'ajout
    message_erreur=""
    if (indrech==-1) :
        message_erreur=message_erreur+"Veuillez vérifier le numéro de CIN saisie\n"
    if (nombreannee.isdigit()==False or int(nombreannee)> int(age)) :
        message_erreur=message_erreur+"Veuillez vérifier le nombre d'année saisie\n"
    if (message_erreur==""):
        m=Maladie("0",cin,maladie,nombreannee)
        dicmal.ajouter(m)
        QMessageBox.information(None, "Validation", "Ajout avec succès")
        uiajoutermaladie.reset_fields()
        QApplication.activeWindow().close()
    else :
        QMessageBox.critical(None, "Erreur", message_erreur)
#supprimer maladie
def fsupprimermaladie():
    maladie=uisupprimermaladie.comboBox.currentText() 
    i=dicmal.recherchemaladie(maladie)
    if(i==-1):
        QMessageBox.critical(None, "Erreur", "Aucune personne ne présente cette maladie dans notre base de données.")
    else:
        dicmal.supprimermaladie(maladie)
        QMessageBox.information(None, "Validation", "Supprimé avec succès !")
        uisupprimermaladie.reset_fields()
        QApplication.activeWindow().close()

#modifier nombre annee

def frecherchecinmaladie():
    cin = uimodifiernbmaladie.lineEdit1.text()
    if len(cin)!=8 or cin.isdigit()==False :
        QMessageBox.critical(None, "Erreur", "Veuillez vérifier le numéro de CIN saisie\n")
    maladie = uimodifiernbmaladie.comboBox.currentText()
    i = dicmal.recherchecinmaladie(cin, maladie)
    return i

def fmodifiernombreannee(i):
    nombreannee = uimodifiernbmaladie.lineEdit3.text()
    i=frecherchecinmaladie()
    if(i==-1):
        QMessageBox.critical(None, "Erreur", "Aucune personne ne présente ce numéro de CIN et cette maladie dans notre base de données.")
    else:
        dicmal.modifiernombreannee(i, nombreannee)
        QMessageBox.information(None, "Validation", "La modification a été effectuée avec succès")
        uimodifierdecespers.reset_fields()
        QApplication.activeWindow().close()
        
#affichage par maladie
def frechercheaffichemaladie():
    maladie = uiaffichageparmaladies.comboBox.currentText()
    i = dicmal.recherchemaladie(maladie)
    if i == -1:
        QMessageBox.critical(None, "Erreur", "Aucune personne ne présente cette maladie dans notre base de données.")
    else:
        list_cin = dicmal.cin_list(maladie)
        noms , prenoms = dicmal.afficher_noms_prenoms(dicper,list_cin)
        
        tableaffichageparmaladies = uiaffichageparmaladies.getTable()
        headerH = ['CIN', 'NOM', 'PRÉNOM']
        
        tableaffichageparmaladies.setRowCount(len(noms))
        tableaffichageparmaladies.setColumnCount(3)
        tableaffichageparmaladies.setHorizontalHeaderLabels(headerH)
        headersize = tableaffichageparmaladies.horizontalHeader()
        headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
         
        for i in range(len(noms)):
            tableaffichageparmaladies.setItem(i, 0, QTableWidgetItem(list_cin[i]))
            tableaffichageparmaladies.setItem(i, 1, QTableWidgetItem(noms[i]))
            tableaffichageparmaladies.setItem(i, 2, QTableWidgetItem(prenoms[i]))

#affichage maladie d une personne
def frechercheaffichagemaladiespersonne():
    cin = uiaffichagemaladiespersonne.linemal.text()
    test=dicmal.rechercheexiste(cin)
    if(test==False):
        QMessageBox.critical(None, "Erreur", "Veuillez vérifier le numéro de CIN saisie\n")
    else:    
        diccin = dicmal.dictionnairecin(cin)
        tableaffichagemaladiespersonne = uiaffichagemaladiespersonne.getTable()
        headerH = ['CIN', 'MALADIE']
        if(diccin is None):
            tableaffichagemaladiespersonne.setItem(0, 0, QTableWidgetItem(cin))
            tableaffichagemaladiespersonne.setItem(0, 1, QTableWidgetItem("******"))
        else:
            nbMaladie = diccin.nbmaladie()
            tableaffichagemaladiespersonne.setRowCount(nbMaladie)
            tableaffichagemaladiespersonne.setColumnCount(2)
            tableaffichagemaladiespersonne.setHorizontalHeaderLabels(headerH)
            headersize = tableaffichagemaladiespersonne.horizontalHeader()
            headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            tableaffichagemaladiespersonne.setItem(0, 0, QTableWidgetItem(cin))
            for j in range(nbMaladie):
                m = diccin.getMaladie(j)
                tableaffichagemaladiespersonne.setItem(j, 1, QTableWidgetItem(m.maladie))
            
#affichage pourcentage            
def frechercheaffichagepourcentage():
    maladie = uirecherchepourcentagechaquemaladie.comboBox.currentText()
    pourcentage = dicmal.pourcentageMaladie(maladie)
    uirecherchepourcentagechaquemaladie.lineEdit_2.setText(str(pourcentage)+' %')
    

#####################################################################################################################################################

##################################################Calcul et affichage#######################################################################
#afficher par nationalite
def calafnbligne(dic):
    nbPersonne1=dic.nbpersonne()
    l=nbPersonne1
    for i in range(nbPersonne1):
        dicpm=dicmal.dictionnairecin(dicper.listcin[i])
        nbPersonne2=dicpm.nbmaladie()
        if(nbPersonne2!=0):
            l=l+nbPersonne2-1
    return l
        
    
def fcalafnat():
    nat=ui2calculetaffichageparnationalite.lineEdit.text()
    indrech=dicper.recherchenat(nat)
    if(indrech==-1):
        QMessageBox.critical(None, "Erreur", "Veuillez vérifier que la nationalité saisie\n")
    else:
        dicnat=dicper.dictionnairenat(nat)
        nbligne=calafnbligne(dicnat)
        tablecalaffnat=ui2calculetaffichageparnationalite.getTable()
        headerH = ['CIN','NON','PRENOM','TEL','NATIONALITE','AGE',"DATE D'INFECTION",'DECEDE','CODE','MALADIE', 'NOMBRE D ANNEE']
        nbPersonne=dicnat.nbpersonne()
        tablecalaffnat.setRowCount(nbligne)
        tablecalaffnat.setColumnCount(11)
        tablecalaffnat.setHorizontalHeaderLabels(headerH)
        headersize=tablecalaffnat.horizontalHeader()
        headersize.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(9, QHeaderView.ResizeToContents)
        headersize.setSectionResizeMode(10, QHeaderView.ResizeToContents)
        l=0
        for i in range(nbPersonne):
            p=dicnat.getPersonne(i)
            tablecalaffnat.setItem(l , 0 , QTableWidgetItem(p.cin))
            tablecalaffnat.setItem(l , 1 , QTableWidgetItem(p.nom))
            tablecalaffnat.setItem(l , 2 , QTableWidgetItem(p.prenom))
            tablecalaffnat.setItem(l , 3 , QTableWidgetItem(p.tel))
            tablecalaffnat.setItem(l , 4 , QTableWidgetItem(p.nationalite))
            tablecalaffnat.setItem(l , 5 , QTableWidgetItem(p.age))
            tablecalaffnat.setItem(l , 6 , QTableWidgetItem(p.dateinfection))
            tablecalaffnat.setItem(l , 7 , QTableWidgetItem(p.decede))
            dicpm=dicmal.dictionnairecin(dicper.listcin[i])
            nbm=dicpm.nbmaladie()
            if(nbm==0):
                tablecalaffnat.setItem(l , 8 , QTableWidgetItem("*****"))
                tablecalaffnat.setItem(l , 9 , QTableWidgetItem("*****"))
                tablecalaffnat.setItem(l , 10 , QTableWidgetItem("*****"))
                l=l+1
            else:
                for j in range(nbm):
                    m=dicpm.getMaladie(j)
                    tablecalaffnat.setItem(l , 8 , QTableWidgetItem(m.code))
                    tablecalaffnat.setItem(l , 9 , QTableWidgetItem(m.maladie))
                    tablecalaffnat.setItem(l , 10 , QTableWidgetItem(m.nombreannee))
                    l=l+1


#############################################################################################################################################
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
#app.aboutToQuit.connect(ui.closeEvent01)
#ajouterpersonne

ajouterpersonne = QtWidgets.QDialog()
uiajouterpersonne = ajouterpersonneDialog()
uiajouterpersonne.setupUi(ajouterpersonne)
#ajoutermaladie
ajoutermaladie = QtWidgets.QDialog()
uiajoutermaladie = ajoutermaladieDialog()
uiajoutermaladie.setupUi(ajoutermaladie)
#suppcin
supprimercin = QtWidgets.QDialog()
uisupprimercin = supprimercinDialog()
uisupprimercin.setupUi(supprimercin)
#supptele
supprimertelephone = QtWidgets.QDialog()
uisupprimertelephone = supprimertelephoneDialog()
uisupprimertelephone.setupUi(supprimertelephone)
#suppnatio
supprimernationalite = QtWidgets.QDialog()
uisupprimernationalite = supprimernationaliteDialog()
uisupprimernationalite.setupUi(supprimernationalite)
#supprimermaladie
supprimermaladie = QtWidgets.QDialog()
uisupprimermaladie = supprimermaladieDialog()
uisupprimermaladie.setupUi(supprimermaladie)
#modifnumpers
modifiernumpers = QtWidgets.QDialog()
uimodifiernumpers = modifiernumpersDialog()
uimodifiernumpers.setupUi(modifiernumpers)
#modifdeces
modifierdecespers = QtWidgets.QDialog()
uimodifierdecespers = modifierdecespersDialog()
uimodifierdecespers.setupUi(modifierdecespers)
#modifnummaladie
modifiernbmaladie = QtWidgets.QDialog()
uimodifiernbmaladie = modifiernbmaladieDialog()
uimodifiernbmaladie.setupUi(modifiernbmaladie)
   
#maladie de chaque personne
affichagemaladieschaquepersonne = QtWidgets.QDialog()
uiaffichagemaladieschaquepersonne = affichagemaladieschaquepersonneForm()
uiaffichagemaladieschaquepersonne.setupUi(affichagemaladieschaquepersonne)
#affichage tous personnes
affichagetouspersonne = QtWidgets.QDialog()
uiaffichagetouspersonne = affichagetouspersonneForm()
uiaffichagetouspersonne.setupUi(affichagetouspersonne)

#affichageaffichagepartelephone
affichagepartelephone = QtWidgets.QDialog()
uiaffichagepartelephone = affichagepartelephoneForm()
uiaffichagepartelephone.setupUi(affichagepartelephone)
#affichageparindicatif
affichageparindicatif = QtWidgets.QDialog()
uiaffichageparindicatif = affichageparindicatifForm()
uiaffichageparindicatif.setupUi(affichageparindicatif)
#affichageparnationalite
affichageparnationalite = QtWidgets.QDialog()
uiaffichageparnationalite = affichageparnationaliteForm()
uiaffichageparnationalite.setupUi(affichageparnationalite)
#affichagepersonnedecedes
affichagepersonnedecedes = QtWidgets.QDialog()
uiaffichagepersonnedecedes = affichagepersonnedecedesForm()
uiaffichagepersonnedecedes.setupUi(affichagepersonnedecedes)
#affichagepersonnenondecedes
affichagepersonnenondecedes = QtWidgets.QDialog()
uiaffichagepersonnenondecedes = affichagepersonnenondecedesForm()
uiaffichagepersonnenondecedes.setupUi(affichagepersonnenondecedes)

#affichagetoutesmaladies
affichagetoutesmaladies = QtWidgets.QDialog()
uiaffichagetoutesmaladies = affichagetoutesmaladiesForm()
uiaffichagetoutesmaladies.setupUi(affichagetoutesmaladies)
#affichageparmaladies
affichageparmaladies = QtWidgets.QDialog()
uiaffichageparmaladies = affichageparmaladiesForm()
uiaffichageparmaladies.setupUi(affichageparmaladies)
#affichage maladies personne
affichagemaladiespersonne = QtWidgets.QDialog()
uiaffichagemaladiespersonne = affichagemaladiespersonneForm()
uiaffichagemaladiespersonne.setupUi(affichagemaladiespersonne)


#recherche du pourcentage maladie
recherchepourcentagechaquemaladie = QtWidgets.QDialog()
uirecherchepourcentagechaquemaladie = recherchepourcentagechaquemaladieForm()
uirecherchepourcentagechaquemaladie.setupUi(recherchepourcentagechaquemaladie)

#verif
calculetaffichage = QtWidgets.QDialog()
uicalculetaffichage = calculetaffichageForm()
uicalculetaffichage.setupUi(calculetaffichage)
#les boutons de calcul et affichage
boutoncalculetaffichageparnationalite=uicalculetaffichage.getboutoncalculetaffichageparnationalite()
boutoncalculetaffichageparnationalite.clicked.connect(affichecalculetaffichageparnationalite)

boutoncalculetaffichagepersonnearisque=uicalculetaffichage.getboutoncalculetaffichagepersonnearisque()
boutoncalculetaffichagepersonnearisque.clicked.connect(affichecalculetaffichagepersonnearisque)

boutoncalculetaffichagepersonnedecedes=uicalculetaffichage.getboutoncalculetaffichagepersonnedecedes()
boutoncalculetaffichagepersonnedecedes.clicked.connect(affichecalculetaffichagepersonnedecedes)

boutoncalculetaffichagepersonneenquarantaine=uicalculetaffichage.getboutoncalculetaffichagepersonneenquarantaine()
boutoncalculetaffichagepersonneenquarantaine.clicked.connect(affichecalculetaffichagepersonneenquarantaine)

#calculetaffichageparnationalite
calculetaffichageparnationalite = QtWidgets.QDialog()
ui2calculetaffichageparnationalite = calculetaffichageparnationaliteForm()
ui2calculetaffichageparnationalite.setupUi(calculetaffichageparnationalite)
#calculetaffichagepersonnearisque
calculetaffichagepersonnearisque = QtWidgets.QDialog()
ui2calculetaffichagepersonnearisque = calculetaffichagepersonnearisqueForm()
ui2calculetaffichagepersonnearisque.setupUi(calculetaffichagepersonnearisque)
#calculetaffichagepersonnedecedes
calculetaffichagepersonnedecedes = QtWidgets.QDialog()
ui2calculetaffichagepersonnedecedes = calculetaffichagepersonnedecedesForm()
ui2calculetaffichagepersonnedecedes.setupUi(calculetaffichagepersonnedecedes)
#calculetaffichagepersonneenquarantaine
calculetaffichagepersonneenquarantaine = QtWidgets.QDialog()
ui2calculetaffichagepersonneenquarantaine = calculetaffichagepersonneenquarantaineForm()
ui2calculetaffichagepersonneenquarantaine.setupUi(calculetaffichagepersonneenquarantaine)

MainWindow.show()

ui.actionAjouter_personne.triggered.connect(afficheajouterpersonne)
ui.actionAjouter_une_nouvelle_maladie.triggered.connect(afficheajoutermaladie)
ui.actionpar_CIN.triggered.connect(affichesupprimercin)
ui.actionpar_T_l_phone.triggered.connect(affichesupprimertelephone)
ui.actionpar_Nationalit.triggered.connect(affichesupprimernationalite)
ui.actionSupprimer_une_maladie.triggered.connect(affichesupprimermaladie)
ui.actionpar_T_l_phone_2.triggered.connect(affichemodifiernumpers)
ui.actiond_c_s.triggered.connect(affichemodifierdecespers)
ui.actionNombre_d_ann_e.triggered.connect(affichemodifiernbmaladie)

ui.actionMaladies_de_chaque_Personne.triggered.connect(afficheaffichagemaladieschaquepersonne)
ui.actiontous_les_Personnes.triggered.connect(afficheaffichagetouspersonne)
ui.actionpar_T_lephone.triggered.connect(affichageaffichagepartelephone)
ui.actionpar_indicatif.triggered.connect(afficheaffichageparindicatif)
ui.actionpar_Nationalit_2.triggered.connect(afficheaffichageparnationalite)
ui.actionpersonnes_d_ced_s.triggered.connect(afficheaffichagepersonnedecedes)
ui.actionpersonne_non_d_c_d_s.triggered.connect(afficheaffichagepersonnenondecedes)
ui.actiontoutes_les_Maladies.triggered.connect(afficheaffichagetoutesmaladies)
ui.actionpar_maladies.triggered.connect(afficheaffichageparmaladies)
ui.actionMaladies_d_une_Personne.triggered.connect(afficheaffichagemaladiespersonne)

ui.actionle_Pourcentage_de_chaque_maladie.triggered.connect(afficherecherchepourcentagechaquemaladie)

#verif
ui.actionopen.triggered.connect(affichecalculetaffichage)
#gestion des fichier
ui.actionEnregistrement_fichier_Personnes.triggered.connect(enregistrer_fichier_personne)
ui.actionR_cup_ration_fichier_Personnes.triggered.connect(recuperer_fichier_personne)
ui.actionEnregistrement_fichier_Maladies.triggered.connect(enregistrer_fichier_maladie)
ui.actionR_cup_ration_fichier_Maladies.triggered.connect(recuperer_fichier_maladie)

#####################################traitement des boutons gestion personne#########################################################
#ajout personne
bouttonajouter=uiajouterpersonne.getbouttonajouterpersonne()
bouttonajouter.clicked.connect(fajouterpersonne)
#supprimer par cin
bouttonsupprimercin=uisupprimercin.getsupprimercin()
bouttonsupprimercin.clicked.connect(fsupprimercin)
#supprimer par nationalite
bouttonsupprimernationalite=uisupprimernationalite.getsupprimernationalite()
bouttonsupprimernationalite.clicked.connect(fsupprimernationalite)
#supprimer par indicatif   
bouttonsupprimerindicatif=uisupprimertelephone.getsupprimertelephone()
bouttonsupprimerindicatif.clicked.connect(fsupprimerindicatif)
#modifier le num evec recherche cin        
bouttonrecherchecin=uimodifiernumpers.getrecherchecin()
bouttonrecherchecin.clicked.connect(frecherchecin)
bouttonmodifiernumpers=uimodifiernumpers.getnumpers()
bouttonmodifiernumpers.clicked.connect(fmodifiernumpers)
#modifier le dece evec recherche cin        
bouttonrecherchedece=uimodifierdecespers.getbouttonrecherchedece()
bouttonrecherchedece.clicked.connect(frecherchecindece)
bouttonmodifierdece=uimodifierdecespers.getbouttonmodifierdece()
bouttonmodifierdece.clicked.connect(fmodifierdece)
#affichage par numero de telephone
bouttonrechafftel=uiaffichagepartelephone.getbouttonrechafftel()
bouttonrechafftel.clicked.connect(frechercheaffichetel)
#affichage par nationalite
bouttonrechaffnat=uiaffichageparnationalite.getbouttonrechaffnat()
bouttonrechaffnat.clicked.connect(frechercheaffichenat)
#affiche par indicatif
bouttonrechaffindc=uiaffichageparindicatif.getbouttonrechaffindc()
bouttonrechaffindc.clicked.connect(frechercheafficheindc)
#####################################################################################################################################

#####################################traitement des boutons gestion maladies#########################################################
bouttonajoutermaladie=uiajoutermaladie.getbouttonajoutermaladie()
bouttonajoutermaladie.clicked.connect(fajoutermaladie)
#supprimermaladiebouton
bouttonsupprimermaladie=uisupprimermaladie.getbouttonsupprimermaladie()
bouttonsupprimermaladie.clicked.connect(fsupprimermaladie)

#modifanneee

bouttonmodifiernombreannee=uimodifiernbmaladie.getbouttonmodifiernombreannee()
bouttonmodifiernombreannee.clicked.connect(fmodifiernombreannee)

#affichage par maladie
bouttonaffichageparmaladie=uiaffichageparmaladies.getbouttonaffichageparmaladie()
bouttonaffichageparmaladie.clicked.connect(frechercheaffichemaladie)

#affichage maladie d'une personne
bouttonrecherchecin=uiaffichagemaladiespersonne.getbouttonrecherchecin()
bouttonrecherchecin.clicked.connect(frechercheaffichagemaladiespersonne)

#affichage pourcentage
bouttonpourcentage=uirecherchepourcentagechaquemaladie.getbouttonpourcentage()
bouttonpourcentage.clicked.connect(frechercheaffichagepourcentage)


##########################################################################################################################################

#########################################traitement des boutons Calcul et affichage########################################################
#afficher par nationalite
bouttoncalafnat=ui2calculetaffichageparnationalite.getbouttonCalAfnat()
bouttoncalafnat.clicked.connect(fcalafnat)
###########################################################################################################################################

sys.exit(app.exec_())

