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


#Exercice 1
#Faire une fonction qui concatene 2 chaines de caractères, en les séparant par une virgule

#Exercice 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractère
#Avec l'ensemble des occurences d'un chiffre e.g. :
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#La fonction(tableau, 0) doit renvoyer "0,4,7", n'hésitez pas à implémenter la première fonction

#Exercice 3
#Renvoyer / afficher un message
msg = str(input("Entrez votre lettre : "))
print (msg)