#Debut

#Admettre une fonction random qui renvoie un nombre entre 1 et 3 et l'associer a la variable choix

#definir la fonction pfc
        #Si choix est egale a 1
            #ALors retourner "Pierre"
        #Si choix est egale a 2
            #ALors retourner "Feuille"
        #Si choix est egale a 3
            #ALors retourner "Ciseaux"

#Initialiser le jeu
    #Assigner a la variable ready le retour de l'execution de la fonction input("Etes-vous prêt ? (oui/non) ") 
        #Si ready est egale "oui", 
            #Alors poursuivre l'execution du programme
        #Sinon, arreter le programme
    
    #Assigner a la variable valeurJoueur le retour de l'execution de la fonction input("Pierre Feuille ou ciseaux ? ")
        #Si valeurJoueur est egale "Pierre"
            #Alors retourner "Pierre"
        #Sinon si valeurJoueur est egale "Feuille"
            #Alors retourner "Feuille"
        #Sinon si valeurJoueur est egale "Ciseaux"
            #Alors retourner "Ciseaux"
        #Sinon si valeurJoueur vaut autre chose
            #Alors renvoyer un message d'erreur 
            #Et proposer de choisir a nouveau

#Definir l'execution du jeu
    #Comparer le retour des variables valeurJoueur et pfc
        #Si valeurJoueur vaut "Pierre" et pfc vaut "Pierre"
            #Alors afficher "Egalite"
        #Sinon Si valeurJoueur vaut "Pierre" et pfc vaut "Feuille"
            #Alors afficher "Defaite du joueur"
        #Sinon Si valeurJoueur vaut "Pierre" et pfc vaut "Ciseaux"
            #Alors afficher "Victoire du joueur" 
        #Sinon Si valeurJoueur vaut "Feuille" et pfc vaut "Pierre"
            #Alors afficher "Victoire du joueur"
        #Sinon Si valeurJoueur vaut "Feuille" et pfc vaut "Feuille"
            #Alors afficher "Egalite"
        #Sinon Si valeurJoueur vaut "Feuille" et pfc vaut "Ciseaux"
            #Alors afficher "Defaite du joueur"
        #Sinon Si valeurJoueur vaut "Ciseaux" et pfc vaut "Pierre"
            #Alors afficher "Defaite du joueur"
        #Sinon Si valeurJoueur vaut "Ciseaux" et pfc vaut "Feuille"
            #Alors afficher "Victoire du joueur"
        #Sinon Si valeurJoueur vaut "Ciseaux" et pfc vaut "Ciseaux"
            #Alors afficher "Egalite"

#Definir une fonction pour relancer le jeu
    #Demander si le joueur veut continuer
        #Si le joueur veut continuer
            #Alors vider la valeur de valeurJoueur
            #Et relancer le programme
        #Sinon arreter le programme    

#Fin


#Ajouter un score ? Systeme de BO ?
