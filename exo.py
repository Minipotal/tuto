#DEBUT

r=12000
s=1250
e=10
rh=230


P1=(((365*3) / (24-(16-8)))*(rh) > r)
P2=(e * s < r)

assertionFinale = P1 == P2
print (assertionFinale)

P3 = ((365*3)/(4-(12-8))*(rh) > r)
P4 = (e * s < r)

assertionFinaleDeux = P3 == P4
print(assertionFinaleDeux)

def retournerSixPlusTrois():
    return 6+3

def retournerSixPlusX(x):
    return 6+x

# ECRIRE "Bonjour Monde"
# Print "Hello World"

retournerSixPlusX(9)
print ("Hello World !")
#FIN

#Exercices a faire

#ajouter les valeurs
x=float(input("Entrez un nombre X : "))
y=float(input("Entrez un nombre Y : "))

#add(x,y)
def additionnerXplusY(x,y):
    return(x+y)
#sub(x,y)
def soustraireXavecY(x,y):
    return(x-y)
#multiply(x,y)
def multiplierXparY(x,y):
    return(x*y)
#divide(x,y)
def diviserXparY(x,y):
    if (y==0):
        print("Division par 0 impossible")
    else:    
        return(x/y)
#modulo(x,y)
def modulerXparY(x,y):
    return(x%y)
#SalaireNet(Brut, coefficient)
def salaireNet(SalaireBrut, Coefficient):
    return(SalaireBrut*Coefficient)
#SalaireParSeconde(salaire horaire, heure par jour ouvré, nb jours ouvré par an)
def salaireParSeconde(salaireHoraire, HeureOuvre, joursOuvres):
    #Calcul du salaire annuel
    salaireAnnuel=salaireHoraire*HeureOuvre*joursOuvres
    #Calcul du temps en seconde annuel
    tempsAnnuel=31536000
    #Calcul du salaire par seconde
    return(salaireAnnuel/tempsAnnuel)
    

#Définir une fonction withdrawFees qui retire un pourcentage a un totoal en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #definir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent / 100)
     #soustraire fees au total
    result = total - fees
     #retourner la valeur obtenue
    return result

    #Definir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > boolean)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis de la fonction publique
    if isPublic:
        #Alors je soustrais 15% de mon salaire brut
        salaireNet = withdrawFees(salaireBrut,15)
    #Sinon je suis un travailleur du secteur privé
    else:
        #Alors je soustrais 23% a mon salaire brut
        salaireNet = withdrawFees(salaireBrut,23)
    #retourner salaireNet
    return salaireNet


prenom = "Alexandre"
nom = "Delaistre"
identite = nom + prenom # retourne "DelaistreAlexandre"

identite + ' ' + prenom # retourne "Delaistre Alexandre"

intergerValue = 342 #Retourne 342
stringIntegerValue = str(342)# retourne "342"