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
    print(x+y)
#sub(x,y)
def soustraireXavecY(x,y):
    print(x-y)
#multiply(x,y)
def multiplierXparY(x,y):
    print(x*y)
#divide(x,y)
def diviserXparY(x,y):
    print(x/y)
#modulo(x,y)
def modulerXparY(x,y):
    print(x%y)
#SalaireNet(Brut, coefficient)
def salaireNet(SalaireBrut, Coefficient):
    print(SalaireBrut*Coefficient)
#SalaireParSeconde(salaire horaire, heure par jour ouvré, nb jours ouvré par an)
def salaireParSeconde(salaireHoraire, HeureOuvre, joursOuvres):
    salaireAnnuel=salaireHoraire*HeureOuvre*joursOuvres
    tempsAnnuel=31536000
    print(salaireAnnuel/tempsAnnuel)
