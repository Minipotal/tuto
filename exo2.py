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

#Debut

#Entrer un premier mot
str1=(input("Entrez votre premier mot : "))
#Entrer un deuxieme mot
str2=(input("Entrez votre deuxieme mot : "))
#concatener les deux mot avec une separation virgule
print(str1,str2,sep=",")

#Fin

#ou alors : exercice 1

def concatWithComma(strA, strB):
    #on s'assure que strA est bien un string
    stringifiedA = str(strA)
    #on s'assure que strB est bien un string
    stringifiedb = str(strB)
    #Retourne strA + ',' + strB
    return strA + ", " + strB

concatWithComma(23, "toto") #Retourne "23, toto"



#Exercice 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractère
#Avec l'ensemble des occurences d'un chiffre e.g. :
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#La fonction(tableau, 0) doit renvoyer "0,4,7", n'hésitez pas à implémenter la première fonction
tableau = [0,1,1,1,0,1,1,0,1]

#Definir la fonction fidIndex qui itere sur le tableau, cherchant l'index
#des differentes occurences de x
def findIndex(tableau, x):
    #Definir i un index de départ
    i=0
    #Definir chaineRetour telle qu'une chaine de caractere vide
    chaineRetour = ''
    #Je defini un boolean tel que firstTurn est true
    firstTurn = "True"
    #Tant que i est different du nombre d'elt dans le tableau
    while i!= len(tableau):
        #Alors j'attribue a une variable la valeur de tableau a l'index i
        selected = tableau[i]
        #Si selected est egale a x ET que firstTurn est true
        if(selected==x & firstTurn=="True"):
            #Alors on assigne a chaineRetour le retour de str(i)

            #Changer la valeur de firstTurn a false
            firstTurn = "False"
        #Sinon si selected egal a x
        elif(selected ==x):
            #Alors j'assigne le retour de concatWithComma tel que : concatWithComma(chaineRetour, i) a chaineRetour
            chaineRetour = concatWithComma(chaineRetour, i)
        #j'incremente i de 1
        i=i+1
#Definir mon index 
    return chaineRetour

#Exercice 3 

#Debut

#Ecrire un message
msg = str(input("Entrez votre message : "))
#Afficher le message
print (msg)

#Fin