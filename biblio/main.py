# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(266, 220, 51, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 561))
        self.label.setStyleSheet("background-image: url(:/newPrefix/main_800_600 .png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuACCEUIL = QtWidgets.QMenu(self.menubar)
        self.menuACCEUIL.setObjectName("menuACCEUIL")
        
        self.menuGestion_des_personnes = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_personnes.setObjectName("menuGestion_des_personnes")
        
        self.menumise_a_jour_des_personnes = QtWidgets.QMenu(self.menuGestion_des_personnes)
        self.menumise_a_jour_des_personnes.setObjectName("menumise_a_jour_des_personnes")
        self.menumise_a_jour_des_personnes.setIcon(QIcon("icon/update.png")) 
        
        self.menuSupprimer_personne = QtWidgets.QMenu(self.menumise_a_jour_des_personnes)
        self.menuSupprimer_personne.setObjectName("menuSupprimer_personne")
        self.menuSupprimer_personne.setIcon(QIcon("icon/remove.png")) 
        
        self.menumodifier_personne = QtWidgets.QMenu(self.menumise_a_jour_des_personnes)
        self.menumodifier_personne.setObjectName("menumodifier_personne")
        self.menumodifier_personne.setIcon(QIcon("icon/misesajour.png")) 

        self.menuRecherche_et_Affichage = QtWidgets.QMenu(self.menuGestion_des_personnes)
        self.menuRecherche_et_Affichage.setObjectName("menuRecherche_et_Affichage")     
        self.menuRecherche_et_Affichage.setIcon(QIcon("icon/search.png"))
      
        
        self.menuGestion_des_maladies = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_maladies.setObjectName("menuGestion_des_maladies")
        
        self.menuMise_a_jour = QtWidgets.QMenu(self.menuGestion_des_maladies)
        self.menuMise_a_jour.setObjectName("menuMise_a_jour")
        self.menuMise_a_jour.setIcon(QIcon("icon/update.png")) 
        
        self.menuModifier_les_donnees_d_une_maladie = QtWidgets.QMenu(self.menuMise_a_jour)
        self.menuModifier_les_donnees_d_une_maladie.setObjectName("menuModifier_les_donnees_d_une_maladie")
        self.menuModifier_les_donnees_d_une_maladie.setIcon(QIcon("icon/misesajour.png")) 
        
        self.menuRecherche_et_Affichage_2 = QtWidgets.QMenu(self.menuGestion_des_maladies)
        self.menuRecherche_et_Affichage_2.setObjectName("menuRecherche_et_Affichage_2")
        self.menuRecherche_et_Affichage_2.setIcon(QIcon("icon/search.png"))
        
        self.menuCalcul_et_Affichage = QtWidgets.QMenu(self.menubar)
        self.menuCalcul_et_Affichage.setObjectName("menuCalcul_et_Affichage")
        
        self.menuEnregistrement_et_R_cup_ration_des_fichiers = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrement_et_R_cup_ration_des_fichiers.setObjectName("menuEnregistrement_et_R_cup_ration_des_fichiers")
        #self.menuEnregistrement_et_R_cup_ration_des_fichiers.setIcon(QIcon("icon/sauvegarder.png"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAfficher_par_nationalit = QtWidgets.QAction(MainWindow)
        self.actionAfficher_par_nationalit.setObjectName("actionAfficher_par_nationalit")
        
        self.actionPersonnes_en_quarantaine = QtWidgets.QAction(MainWindow)
        self.actionPersonnes_en_quarantaine.setObjectName("actionPersonnes_en_quarantaine")
        
        self.actionPersonnes_d_c_d_s = QtWidgets.QAction(MainWindow)
        self.actionPersonnes_d_c_d_s.setObjectName("actionPersonnes_d_c_d_s")
        
        self.actionPersonnes_a_risque = QtWidgets.QAction(MainWindow)
        self.actionPersonnes_a_risque.setObjectName("actionPersonnes_a_risque")
        
        self.actionEnregistrement_fichier_Personnes = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_fichier_Personnes.setObjectName("actionEnregistrement_fichier_Personnes")
        self.actionEnregistrement_fichier_Personnes.setIcon(QIcon("icon/database.png"))
        
        self.actionR_cup_ration_fichier_Personnes = QtWidgets.QAction(MainWindow)
        self.actionR_cup_ration_fichier_Personnes.setObjectName("actionR_cup_ration_fichier_Personnes")
        self.actionR_cup_ration_fichier_Personnes.setIcon(QIcon("icon/recover.png"))
        
        self.actionEnregistrement_fichier_Maladies = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_fichier_Maladies.setObjectName("actionEnregistrement_fichier_Maladies")
        self.actionEnregistrement_fichier_Maladies.setIcon(QIcon("icon/database.png"))
        
        self.actionR_cup_ration_fichier_Maladies = QtWidgets.QAction(MainWindow)
        self.actionR_cup_ration_fichier_Maladies.setObjectName("actionR_cup_ration_fichier_Maladies")
        self.actionR_cup_ration_fichier_Maladies.setIcon(QIcon("icon/recover.png"))
        
        self.actionAjouter_personne = QtWidgets.QAction(MainWindow)
        self.actionAjouter_personne.setObjectName("actionAjouter_personne")
        self.actionAjouter_personne.setIcon(QIcon("icon/adduser.png"))
        
        self.actionAjouter_une_nouvelle_maladie = QtWidgets.QAction(MainWindow)
        self.actionAjouter_une_nouvelle_maladie.setObjectName("actionAjouter_une_nouvelle_maladie")
        self.actionAjouter_une_nouvelle_maladie.setIcon(QIcon("icon/bed.png"))
        
        self.actionSupprimer_une_maladie = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_maladie.setObjectName("actionSupprimer_une_maladie")
        self.actionSupprimer_une_maladie.setIcon(QIcon("icon/delete.png"))
        
        self.actionpar_CIN = QtWidgets.QAction(MainWindow)
        self.actionpar_CIN.setObjectName("actionpar_CIN")
        self.actionpar_CIN.setIcon(QIcon("icon/id.png"))
        
        self.actionpar_Nationalit = QtWidgets.QAction(MainWindow)
        self.actionpar_Nationalit.setObjectName("actionpar_Nationalit")
        self.actionpar_Nationalit.setIcon(QIcon("icon/flag.png"))
        
        self.actionpar_T_l_phone = QtWidgets.QAction(MainWindow)
        self.actionpar_T_l_phone.setObjectName("actionpar_T_l_phone")
        self.actionpar_T_l_phone.setIcon(QIcon("icon/phone.png"))
        
        self.actionpar_T_l_phone_2 = QtWidgets.QAction(MainWindow)
        self.actionpar_T_l_phone_2.setObjectName("actionpar_T_l_phone_2")
        self.actionpar_T_l_phone_2.setIcon(QIcon("icon/indicatif.png"))

        
        self.actiontous_les_Personnes = QtWidgets.QAction(MainWindow)
        self.actiontous_les_Personnes.setObjectName("actiontous_les_Personnes")
        self.actiontous_les_Personnes.setIcon(QIcon("icon/group.png"))


        self.actionpar_T_lephone = QtWidgets.QAction(MainWindow)
        self.actionpar_T_lephone.setObjectName("actionpar_T_lephone")
        self.actionpar_T_lephone.setIcon(QIcon("icon/phone.png"))

        
        self.actionpar_indicatif = QtWidgets.QAction(MainWindow)
        self.actionpar_indicatif.setObjectName("actionpar_indicatif")
        self.actionpar_indicatif.setIcon(QIcon("icon/indicatif.png"))


        self.actionpar_Nationalit_2 = QtWidgets.QAction(MainWindow)
        self.actionpar_Nationalit_2.setObjectName("actionpar_Nationalit_2")
        self.actionpar_Nationalit_2.setIcon(QIcon("icon/flag.png"))

        self.actionpersonnes_d_ced_s = QtWidgets.QAction(MainWindow)
        self.actionpersonnes_d_ced_s.setObjectName("actionpersonnes_d_ced_s")
        self.actionpersonnes_d_ced_s.setIcon(QIcon("icon/dead.png"))
        
        
        self.actionpersonne_non_d_c_d_s = QtWidgets.QAction(MainWindow)
        self.actionpersonne_non_d_c_d_s.setObjectName("actionpersonne_non_d_c_d_s")
        self.actionpersonne_non_d_c_d_s.setIcon(QIcon("icon/person.png"))

        
        self.actionNombre_d_ann_e = QtWidgets.QAction(MainWindow)
        self.actionNombre_d_ann_e.setObjectName("actionNombre_d_ann_e")
        self.actionNombre_d_ann_e.setIcon(QIcon("icon/year.png"))
        
        self.actionmodifier_d_c_s = QtWidgets.QAction(MainWindow)
        self.actionmodifier_d_c_s.setObjectName("actionmodifier_d_c_s")
        
        self.actiontoutes_les_Maladies = QtWidgets.QAction(MainWindow)
        self.actiontoutes_les_Maladies.setObjectName("actiontoutes_les_Maladies")
        self.actiontoutes_les_Maladies.setIcon(QIcon("icon/virus.png"))
        
        self.actionpar_maladies = QtWidgets.QAction(MainWindow)
        self.actionpar_maladies.setObjectName("actionpar_maladies")
        self.actionpar_maladies.setIcon(QIcon("icon/bacteria.png"))

        
        self.actionMaladies_d_une_Personne = QtWidgets.QAction(MainWindow)
        self.actionMaladies_d_une_Personne.setObjectName("actionMaladies_d_une_Personne")
        self.actionMaladies_d_une_Personne.setIcon(QIcon("icon/person.png"))
        
        self.actionle_Pourcentage_de_chaque_maladie = QtWidgets.QAction(MainWindow)
        self.actionle_Pourcentage_de_chaque_maladie.setObjectName("actionle_Pourcentage_de_chaque_maladie")
        self.actionle_Pourcentage_de_chaque_maladie.setIcon(QIcon("icon/%.png"))
        
        self.actionMaladies_de_chaque_Personne = QtWidgets.QAction(MainWindow)
        self.actionMaladies_de_chaque_Personne.setObjectName("actionMaladies_de_chaque_Personne")
        self.actionMaladies_de_chaque_Personne.setIcon(QIcon("icon/sick.png"))
        
        self.actiond_c_s = QtWidgets.QAction(MainWindow)
        self.actiond_c_s.setObjectName("actiond_c_s")
        self.actiond_c_s.setIcon(QIcon("icon/dead.png"))
        
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen.setIcon(QIcon("icon/click.png"))
        
        
        
        
        self.menuSupprimer_personne.addAction(self.actionpar_CIN)
        self.menuSupprimer_personne.addAction(self.actionpar_Nationalit)
        self.menuSupprimer_personne.addAction(self.actionpar_T_l_phone)
        self.menumodifier_personne.addAction(self.actionpar_T_l_phone_2)
        self.menumodifier_personne.addAction(self.actiond_c_s)
        self.menumise_a_jour_des_personnes.addAction(self.actionAjouter_personne)
        self.menumise_a_jour_des_personnes.addAction(self.menuSupprimer_personne.menuAction())
        self.menumise_a_jour_des_personnes.addAction(self.menumodifier_personne.menuAction())
        self.menuRecherche_et_Affichage.addAction(self.actiontous_les_Personnes)
        self.menuRecherche_et_Affichage.addAction(self.actionpar_T_lephone)
        self.menuRecherche_et_Affichage.addAction(self.actionpar_indicatif)
        self.menuRecherche_et_Affichage.addAction(self.actionpar_Nationalit_2)
        self.menuRecherche_et_Affichage.addAction(self.actionpersonnes_d_ced_s)
        self.menuRecherche_et_Affichage.addAction(self.actionpersonne_non_d_c_d_s)
        self.menuGestion_des_personnes.addAction(self.menumise_a_jour_des_personnes.menuAction())
        self.menuGestion_des_personnes.addAction(self.menuRecherche_et_Affichage.menuAction())
        self.menuModifier_les_donnees_d_une_maladie.addAction(self.actionNombre_d_ann_e)
        self.menuMise_a_jour.addAction(self.actionAjouter_une_nouvelle_maladie)
        self.menuMise_a_jour.addAction(self.actionSupprimer_une_maladie)
        self.menuMise_a_jour.addAction(self.menuModifier_les_donnees_d_une_maladie.menuAction())
        self.menuRecherche_et_Affichage_2.addAction(self.actiontoutes_les_Maladies)
        self.menuRecherche_et_Affichage_2.addAction(self.actionpar_maladies)
        self.menuRecherche_et_Affichage_2.addAction(self.actionMaladies_d_une_Personne)
        self.menuRecherche_et_Affichage_2.addAction(self.actionle_Pourcentage_de_chaque_maladie)
        self.menuRecherche_et_Affichage_2.addAction(self.actionMaladies_de_chaque_Personne)
        self.menuGestion_des_maladies.addAction(self.menuMise_a_jour.menuAction())
        self.menuGestion_des_maladies.addAction(self.menuRecherche_et_Affichage_2.menuAction())
        self.menuCalcul_et_Affichage.addAction(self.actionopen)
        self.menuEnregistrement_et_R_cup_ration_des_fichiers.addAction(self.actionEnregistrement_fichier_Personnes)
        self.menuEnregistrement_et_R_cup_ration_des_fichiers.addAction(self.actionR_cup_ration_fichier_Personnes)
        self.menuEnregistrement_et_R_cup_ration_des_fichiers.addAction(self.actionEnregistrement_fichier_Maladies)
        self.menuEnregistrement_et_R_cup_ration_des_fichiers.addAction(self.actionR_cup_ration_fichier_Maladies)
        self.menubar.addAction(self.menuACCEUIL.menuAction())
        self.menubar.addAction(self.menuGestion_des_personnes.menuAction())
        self.menubar.addAction(self.menuGestion_des_maladies.menuAction())
        self.menubar.addAction(self.menuCalcul_et_Affichage.menuAction())
        self.menubar.addAction(self.menuEnregistrement_et_R_cup_ration_des_fichiers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestion des personnes infectées par le virus CORONA"))
        self.menuACCEUIL.setTitle(_translate("MainWindow", "ACCEUIL"))
        self.menuGestion_des_personnes.setTitle(_translate("MainWindow", "Gestion des personnes"))
        self.menumise_a_jour_des_personnes.setTitle(_translate("MainWindow", "mise à jour des personnes"))
        self.menuSupprimer_personne.setTitle(_translate("MainWindow", "Supprimer personne"))
        self.menumodifier_personne.setTitle(_translate("MainWindow", "modifier personne"))
        self.menuRecherche_et_Affichage.setTitle(_translate("MainWindow", "Recherche et Affichage"))
        self.menuGestion_des_maladies.setTitle(_translate("MainWindow", "Gestion des maladies"))
        self.menuMise_a_jour.setTitle(_translate("MainWindow", "Mise à jour"))
        self.menuModifier_les_donnees_d_une_maladie.setTitle(_translate("MainWindow", "Modifier les donnees d\'une maladie"))
        self.menuRecherche_et_Affichage_2.setTitle(_translate("MainWindow", "Recherche et Affichage"))
        self.menuCalcul_et_Affichage.setTitle(_translate("MainWindow", "Calcul et Affichage"))
        self.menuEnregistrement_et_R_cup_ration_des_fichiers.setTitle(_translate("MainWindow", "Gestion des fichiers"))
        self.actionAfficher_par_nationalit.setText(_translate("MainWindow", "Afficher par nationalité"))
        self.actionPersonnes_en_quarantaine.setText(_translate("MainWindow", "Personnes en quarantaine"))
        self.actionPersonnes_d_c_d_s.setText(_translate("MainWindow", "Personnes décédés"))
        self.actionPersonnes_a_risque.setText(_translate("MainWindow", "Personnes a risque"))
        self.actionEnregistrement_fichier_Personnes.setText(_translate("MainWindow", "Enregistrement fichier Personnes"))
        self.actionR_cup_ration_fichier_Personnes.setText(_translate("MainWindow", "Récupération fichier Personnes"))
        self.actionEnregistrement_fichier_Maladies.setText(_translate("MainWindow", "Enregistrement fichier Maladies"))
        self.actionR_cup_ration_fichier_Maladies.setText(_translate("MainWindow", "Récupération fichier Maladies"))
        self.actionAjouter_personne.setText(_translate("MainWindow", "Ajouter personne"))
        self.actionAjouter_une_nouvelle_maladie.setText(_translate("MainWindow", "Ajouter une nouvelle maladie"))
        self.actionSupprimer_une_maladie.setText(_translate("MainWindow", "Supprimer une maladie"))
        self.actionpar_CIN.setText(_translate("MainWindow", "par CIN"))
        self.actionpar_Nationalit.setText(_translate("MainWindow", "par Nationalité"))
        self.actionpar_T_l_phone.setText(_translate("MainWindow", "par Téléphone"))
        self.actionpar_T_l_phone_2.setText(_translate("MainWindow", "par Indicatif"))
        self.actiontous_les_Personnes.setText(_translate("MainWindow", "tous les  Personnes"))
        self.actionpar_T_lephone.setText(_translate("MainWindow", "par Télephone"))
        self.actionpar_indicatif.setText(_translate("MainWindow", "par Indicatif"))
        self.actionpar_Nationalit_2.setText(_translate("MainWindow", "par Nationalité"))
        self.actionpersonnes_d_ced_s.setText(_translate("MainWindow", "personnes décédés"))
        self.actionpersonne_non_d_c_d_s.setText(_translate("MainWindow", "personne non décédés"))
        self.actionNombre_d_ann_e.setText(_translate("MainWindow", "Nombre d\'année"))
        self.actionmodifier_d_c_s.setText(_translate("MainWindow", "modifier décès"))
        self.actiontoutes_les_Maladies.setText(_translate("MainWindow", "toutes les Maladies"))
        self.actionpar_maladies.setText(_translate("MainWindow", "par Maladies"))
        self.actionMaladies_d_une_Personne.setText(_translate("MainWindow", "Maladies d\'une Personne"))
        self.actionle_Pourcentage_de_chaque_maladie.setText(_translate("MainWindow", "le Pourcentage de chaque maladie"))
        self.actionMaladies_de_chaque_Personne.setText(_translate("MainWindow", "Maladies de chaque Personne"))
        self.actiond_c_s.setText(_translate("MainWindow", "décès"))
        self.actionopen.setText(_translate("MainWindow", "ouvrir"))
    
"""    def closeEvent01(self):
        print("close01")
        from PyQt5.QtCore import QEvent
        event = QEvent(QEvent.Close)
        
        # Ignore l'événement de fermeture
        event.ignore()
        # Appelle la méthode closeEvent avec l'événement factice
        self.closeEvent(event)
        
    def closeEvent(self, event):
        print("close02")
        reply = QMessageBox.question(self.window, 'Fermeture de la fenêtre', 'Êtes-vous sûr de vouloir fermer la fenêtre ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #reply =QMessageBox.question(self, 'Fermeture de la fenêtre', 'Êtes-vous sûr de vouloir fermer la fenêtre ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            super().closeEvent(event)
        else:
            event.ignore()
"""        
        

        
from photo import photos1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
