from cell import Cell

#trzeba naprawić  to, że komóki updatują się po kolei, muszą jednocześnie

def printMatrix(matrix):
    lines = []
    for i in range(20):
        lines.append('')
        for j in range(20):
            lines[i] += str(matrix[i][j].life)
        print(lines[i])

myArray = [[0 for x in range(20)] for y in range(20)]

for i in range(20):
    for j in range(20):
        myArray[i][j] = Cell()
        myArray[i][j].x = i
        myArray[i][j].y = j
        myArray[i][j].life = myArray[i][j].setLife()

printMatrix(myArray)
print('\n')

while (input() != "end"):
    for i in range(20):
        for j in range(20):
            myArray[i][j].neighbours_alive = myArray[i][j].check_neighbours(myArray, myArray[i][j].x, myArray[i][j].y)

    for i in range(20):
        for j in range(20):
            myArray[i][j].life = myArray[i][j].update(myArray[i][j].life, myArray[i][j].neighbours_alive)


    printMatrix(myArray)
