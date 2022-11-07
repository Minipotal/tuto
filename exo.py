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