#START

#On admet une fonction Grid qui va créer un tableau de jeu
def afficherGrille(grille):
    #On écrit 1 2 3 pour définir les colonnes et les lignes
    print("     1)  2)  3)")
    #on créé une ligne 
    print("   -------------")
    #on créé une colonne en choissisant le charactère barre verticale et en le duplicant 
    print("1)", end='')
    for i in range(3):
      print(" | "+str(grille[i]), end='')
    print(" |")
    #on créé une ligne 
    print("   -------------")
    #on créé une colonne en choissisant le charactère barre verticale et en le duplicant
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    #on créé une ligne
    print("   -------------")
    #on créé une colonne en choissisant le charactère barre verticale et en le duplicant 
    print("3)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    #on créé une ligne
    print("   -------------")

#On admet une gestion qui définit quel joueur doit jouer quand
def tourJoueur(grille, joueur):
    #on affiche un message indiquant quel joueur doit jouer
    print("C'est au joueur "+str(joueur)+" de jouer son tour")
    #on demande ensuite au joueur de choisir sa colonne
    colonneJouee=input("Joueur "+str(joueur)+", quel est ton choix de colonne ?")
    colonneJoueeTab = int(colonneJouee)-1
    #on demande au joueur de choisir sa ligne 
    ligneJouee=input("Joueur "+str(joueur)+", quel est ton choix de ligne ?")
    #On affiche au joueur la case jouer
    ligneJoueeTab = int(ligneJouee)-1
    print("Joueur "+str(joueur)+", vous avez joué la case "+str(colonneJouee)+","+str(ligneJouee))
    #on créé une boucle qui vérifie que la case soit vide
        #tant que la case n'est pas vide 
    while grille[int(colonneJoueeTab)+int(ligneJoueeTab)*3] != ' ':
        # if ligneJouee ==0 or colonneJouee==0:
            #afficher un message indiquant que la case est prise
            print("La case que vous tentez de jouer est djà prise !")
            #demander au joueur sa colonne
            colonneJouee=input("Joueur "+str(joueur)+", quel est ton nouveau choix de colonne ?")
            #demander au joueur sa ligne
            ligneJouee=input("Joueur "+str(joueur)+", quel est ton nouveau choix de ligne ?")
            #afficher la case joueur
            print("Joueur "+str(joueur)+", vous avez joué la case "+str(colonneJouee)+","+str(ligneJouee))

    #Si le joueur est le numéro 1
    if joueur == 1:
        #alors son token sera une croix
        grille[int(colonneJoueeTab)+int(ligneJoueeTab)*3]="X"
    #Si le joueur est le numéro 2
    if joueur == 2: 
        #alors son token sera un rond
        grille[int(colonneJoueeTab)+int(ligneJoueeTab)*3]="O"
    afficherGrille(grille)

#On admet une fonction conditionVictoire qui prend en paramètre la grille et vérifie le placement des tokens pour déclarer la victoire
def conditionVictoire(grille):

    #si la ligne horizontale est vérifiée
    if (grille[0]==grille[1]==grille[2]!=" " or grille[3]==grille[4]==grille[5]!=" " or grille[6]==grille[7]==grille[8]!=" "):
        #Alors retourner 1
        return 1

    #si la ligne verticale est vérifiée
    if (grille[0]==grille[3]==grille[6]!=" " or grille[1]==grille[4]==grille[7]!=" " or grille[2]==grille[5]==grille[8]!=" "):
        #Alors retourner 1
        return 1

    #si la ligne diagonale est vérifiée
    if (grille[0]==grille[4]==grille[8]!=" " or grille[2]==grille[4]==grille[6]!=" "):
        #Alors retourner 1
        return 1
        
def matchNul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1


joueur=1
print("Le joueur 1 jouera avec les X. Le joueur 2 jouera avec les O")
grille=[" "," "," "," "," "," "," "," "," "]
afficherGrille(grille)
gagne=0
while gagne==0:
    tourJoueur(grille,joueur)
    if conditionVictoire(grille):
        print("Le joueur "+str(joueur)+" remporte la partie")
        gagne=1
    else:
        if matchNul(grille):
            print("Plus de place ! Match nul !")
            gagne=1
    if joueur==1:
        joueur=2
    else:
        joueur=1
#END
