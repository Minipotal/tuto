#START
 
from random import *
#from math import *

print("Bienvenue au morpion")
print("----------------------")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

### Definir la fonction pour check qui a gagné
def checkForWinner(gameBoard):
  ### X axis
  if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
    print("O a gagné!")
    return "O"
  elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
    print("O a gagné!")
    return "O"
  elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O a gagné!")
    return "O"
  ### Y axis
  if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
    print("O a gagné!")
    return "O"
  elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
    print("O a gagné!")
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
    print("O a gagné!")
    return "O"
  ### Croix gagne
  elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X a gagné!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O a gagné!")  
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
    print("X a gagné!")  
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
    print("O a gagné!") 
    return "O" 
  else:
    return "N"

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

globalElementCheck = [
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [2, 2]],
[[2, 0], [1, 1], [0, 2]]]



leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  ### C'est le tour du joueur
  if(turnCounter % 2 == 0):
    printGameBoard()
    numberPicked = int(input("\nChoisissez un nombre [1-9]: "))
    if(numberPicked >= 1 or numberPicked <= 9):
      modifyArray(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
    else:
      print("Charcatère invalide. Essayez à nouveau.")
    turnCounter += 1
  ###L'ordinateur joue
  else:
    while(True):
      cpuChoice = random.choice(possibleNumbers)
      print("\nChoix du cpu: ", cpuChoice)
      if(cpuChoice in possibleNumbers):
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
    print("\nLa partie est finie! Merci d'avoir joué :)\n")
    break
#END