#START
 
from random import *

print("Bienvenue au morpion")
print("----------------------")

nombresJouables = [1,2,3,4,5,6,7,8,9]
tab = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
nbl = 3
nbc = 3

def printTab():
  for x in range(nbl):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(nbc):
      print("", tab[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    tab[0][0] = turn
  elif(num == 1):
    tab[0][1] = turn
  elif(num == 2):
    tab[0][2] = turn
  elif(num == 3):
    tab[1][0] = turn
  elif(num == 4):
    tab[1][1] = turn
  elif(num == 5):
    tab[1][2] = turn
  elif(num == 6):
    tab[2][0] = turn
  elif(num == 7):
    tab[2][1] = turn
  elif(num == 8):
    tab[2][2] = turn

### Definir la fonction pour check qui a gagné
def checkerVainqueur(tab):
  ### X axis
  if(tab[0][0] == 'X' and tab[0][1] == 'X' and tab[0][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[0][0] == 'O' and tab[0][1] == 'O' and tab[0][2] == 'O'):
    print("O a gagné!")
    return "O"
  elif(tab[1][0] == 'X' and tab[1][1] == 'X' and tab[1][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[1][0] == 'O' and tab[1][1] == 'O' and tab[1][2] == 'O'):
    print("O a gagné!")
    return "O"
  elif(tab[2][0] == 'X' and tab[2][1] == 'X' and tab[2][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[2][0] == 'O' and tab[2][1] == 'O' and tab[2][2] == 'O'):
    print("O a gagné!")
    return "O"
  ### Y axis
  if(tab[0][0] == 'X' and tab[1][0] == 'X' and tab[2][0] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[0][0] == 'O' and tab[1][0] == 'O' and tab[2][0] == 'O'):
    print("O a gagné!")
    return "O"
  elif(tab[0][1] == 'X' and tab[1][1] == 'X' and tab[2][1] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[0][1] == 'O' and tab[1][1] == 'O' and tab[2][1] == 'O'):
    print("O a gagné!")
    return "O"
  elif(tab[0][2] == 'X' and tab[1][2] == 'X' and tab[2][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[0][2] == 'O' and tab[1][2] == 'O' and tab[2][2] == 'O'):
    print("O a gagné!")
    return "O"
  ### Croix gagne
  elif(tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(tab[0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O'):
    print("O a gagné!")  
    return "O"
  elif(tab[0][2] == 'X' and tab[1][1] == 'X' and tab[2][0] == 'X'):
    print("X a gagné!")  
    return "X"
  elif(tab[0][2] == 'O' and tab[1][1] == 'O' and tab[2][0] == 'O'):
    print("O a gagné!") 
    return "O" 
  else:
    return "N"


"""Tentative d'Ia

def position(i,p):
  if gameBoard [i][p] == 'X':
    return 1
  elif gameBoard [i][p] == 'O':
    return -2
  else: return 0 


def ordinateur():
  tab = [0*8]
  tab [0] = position(0,0) + position(0,1) + position(0,2)
  tab [1] = position(1,0) + position(1,1) + position(1,2)
  tab [2] = position(2,0) + position(2,1) + position(2,2)
  tab [3] = position(0,0) + position(1,0) + position(2,0)
  tab [4] = position(0,1) + position(1,1) + position(2,1)
  tab [5] = position(0,2) + position(1,2) + position(2,2)
  tab [6] = position(0,0) + position(1,1) + position(2,2)
  tab [7] = position(2,0) + position(1,1) + position(0,2)

  mini = 0

  for i in range(8):
    val = tab[i]
    if ((val < 0) and (abs(val)%2 == 0) and (val < tab[mini])):
      mini = i
"""


boucleJeu = False
compteurTour = 0

while(boucleJeu == False):
  ### C'est le tour du joueur
  if(compteurTour % 2 == 0):
    printTab()
    nombreChoisi = int(input("\nChoisissez un nombre [1-9]: "))
    if(nombreChoisi >= 1 or nombreChoisi <= 9):
      modifyArray(nombreChoisi, 'X')
      nombresJouables.remove(nombreChoisi)
    else:
      print("Caractère invalide. Essayez à nouveau.")
    compteurTour += 1
  ###L'ordinateur
  else:
    while(True):
      cpuChoix = choice(nombresJouables)
      print("\nChoix du cpu: ", cpuChoix)
      if(cpuChoix in nombresJouables):
        modifyArray(cpuChoix, 'O')
        nombresJouables.remove(cpuChoix)
        compteurTour += 1
        break
  
  winner = checkerVainqueur(tab)
  if(winner != "N"):
    print("\nLa partie est finie! Merci d'avoir joué :)\n")
    break
#END