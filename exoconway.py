def generateTable(L):
    return[[(str(x) + '_' + str(y)) for x in range(L)] for y in range(L)]

def displayTable(table):
    for i in table:
        print(i)

connwayBoard = generateTable(5)

displayTable(connwayBoard)