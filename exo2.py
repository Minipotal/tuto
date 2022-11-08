#def input():
    # Exercice
    # Faire un mini jeu qui affiche un message lorsque input envoie le bon caractère
    # le caractère doit etre parametrable

    # Debut
    # Definir le caractère a trouver


#Definir une lettre aleatoire
import random , string
letter = random.choice(string.ascii_lowercase)


# Initialiser un compteur
compteur = 0

# Verifier le caractère renvoyé par input tant que la valeur envoyée est différente de la valeur recherchée
while str(input("Entrez votre lettre : ")) != letter:
    # incrémenter le compteur
    
    compteur = compteur + 1
    # letter = str(input("Entrez votre lettre : "))
else:
    # Afficher un message disant que la lettre a été trouvée ainsi que le compteur
    print("Bravo, vous avez trouvé la lettre recherchée. Tentatives : "+str(compteur))

    # vider le compteur
compteur = 0
letter=" "
# Fin
