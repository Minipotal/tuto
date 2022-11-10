#Debut

#Definir la fonction de la suite de fibonacci
def fibonacci(n):
    #Si n inferieur a 1, pas de suite possible
    if(n <= 1):
        #Retourner n
        return n
    #Sinon calculer la suite de fibonacci
    else:
        #Retourner la somme du terme ainsi que son precedent
        return (fibonacci(n-1) + fibonacci(n-2))

#definir combien de passage
n = int(input("Entrez le nombre de termes:"))
#Afficher la suite de fibonacci
def suite(strA,strB):
    #on s'assure que strA est bien un string
    stringifiedA = str(strA)
    #on s'assure que strB est bien un string
    stringifiedb = str(strB)
    #Retourne strA + ',' + strB
    return strA + ", " + strB

firstTurn = "True"

#Definir la boucle recursive
for i in range(n):
    if firstTurn == "True":
        chaineRetour = 'Suite de Fibonacci : 0'
        firstTurn = "False"
    else:
        etape =str(fibonacci(i))
        chaineRetour = suite(chaineRetour, etape)
    
    #print(fibonacci(i))
if(n <= 1):
    print("Choisissez au minimum 1")
else:
    print(chaineRetour)
    
#Fin