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
print("Suite de Fibonacci en utilisant la recursion :")
#Definir la boucle recursive
for i in range(n):
    #Calculer la fonction a l'instant i
    print(fibonacci(i))
    
#Fin