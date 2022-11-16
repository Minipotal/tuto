from random import *


# Admettre une fonction random qui renvoie un nombre entre 1 et 3 et l'associer a la variable choix
def rndChoice():
    choix = randint(1, 3)
    return choix


def pfc(choix):
    if choix == 1:
        pc = "Pierre"
    elif choix == 2:
        pc = "Feuille"
    elif choix == 3:
        pc = "Ciseaux"
    return (pc)

# Initialiser le jeu


def choixJoueur():
    # Assigner a la variable ready le retour de l'execution de la fonction input("Etes-vous prêt ? (oui/non) ")
    ready = str(input("Êtes-vous prêt a jouer ? (oui/non) "))
    # Si ready est egale "oui",
    if ready == "oui":
        # Alors poursuivre l'execution du programme
        # Assigner a la variable valeurJoueur le retour de l'execution de la fonction input("Pierre Feuille ou ciseaux ? ")
        valeurJoueur = str(
            input("Saisissez votre choix (Pierre, Feuille ou Ciseaux) : "))
        # si valeurJoueur vaut autre chose
        while valeurJoueur not in ["Pierre", "Feuille", "Ciseaux"]:
            # Alors renvoyer un message d'erreur
            print("Veuillez entrer une valeur comprise dans la sélection")
            valeurJoueur = str(
                input("Saisissez votre choix (Pierre, Feuille ou Ciseaux) : "))
        return (valeurJoueur)

    elif ready == "non":
        exit()
    else:
        input("Cas inconnu")
        exit()


rnd = rndChoice()
pc = pfc(rnd)
joueur = choixJoueur()


# Definir l'execution du jeu
def jeu(valeurJoueur, choix):
    # Si valeurJoueur vaut "Pierre" et pfc vaut "Pierre"
    if valeurJoueur == "Pierre" and choix == "Pierre":
        # Alors afficher "Egalite"
        print("Egalite")
    # Sinon Si valeurJoueur vaut "Pierre" et pfc vaut "Feuille"
    if valeurJoueur == "Pierre" and choix == "Feuille":
        # Alors afficher "Defaite du joueur"
        print("Défaite du joueur")
    # Sinon Si valeurJoueur vaut "Pierre" et pfc vaut "Ciseaux"
    if valeurJoueur == "Pierre" and choix == "Ciseaux":
        # Alors afficher "Victoire du joueur"
        print("Victoire du joueur")

    # Sinon Si valeurJoueur vaut "Feuille" et pfc vaut "Pierre"
    if valeurJoueur == "Feuille" and choix == "Pierre":
        # Alors afficher "Victoire du joueur"
        print("Victoire du joueur")
    # Sinon Si valeurJoueur vaut "Feuille" et pfc vaut "Feuille"
    if valeurJoueur == "Feuille" and choix == "Feuille":
        # Alors afficher "Egalite"
        print("Egalite")
    # Sinon Si valeurJoueur vaut "Feuille" et pfc vaut "Ciseaux"
    if valeurJoueur == "Feuille" and choix == "Ciseaux":
        # Alors afficher "Defaite du joueur"
        print("Défaite du joueur")

    # Sinon Si valeurJoueur vaut "Ciseaux" et pfc vaut "Pierre"
    if valeurJoueur == "Ciseaux" and choix == "Pierre":
        # Alors afficher "Defaite du joueur"
        print("Défaite du joueur")
    # Sinon Si valeurJoueur vaut "Ciseaux" et pfc vaut "Feuille"
    if valeurJoueur == "Ciseaux" and choix == "Feuille":
        # Alors afficher "Victoire du joueur"
        print("Victoire du joueur")
    # Sinon Si valeurJoueur vaut "Ciseaux" et pfc vaut "Ciseaux"
    if valeurJoueur == "Ciseaux" and choix == "Ciseaux":
        # Alors afficher "Egalite"
        print("Egalite")


jeu(joueur, pc)
print("Le pc a choisi "+pc+", le joueur a choisi "+joueur)
