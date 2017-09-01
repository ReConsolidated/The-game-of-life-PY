from random import randint

class Cell:
    x = 0
    y = 0
    neighbours_alive = 0
    life = 0
    def setLife(self):
        life = randint(0,1)
        if (life==1):
            life = randint(0,1)
            if (life==1):
                life = randint(0,1)
        return life


    def check_neighbours(self, matrix, x, y):
        neighbours_alive = 0
        if (x-1 >= 0):
            if(y-1 >= 0):
                if (matrix[x-1][y-1].life == 1):
                    neighbours_alive += 1
            if(y+1 <= 19):
                if (matrix[x-1][y+1].life == 1):
                    neighbours_alive += 1
            if (matrix[x-1][y].life == 1):
                neighbours_alive += 1
        if (x+1 <= 19):
            if(y-1 >= 0):
                if (matrix[x+1][y-1].life == 1):
                    neighbours_alive += 1
            if (matrix[x+1][y].life == 1):
                neighbours_alive += 1
            if (y+1 <= 19):
                if (matrix[x+1][y+1].life == 1):
                    neighbours_alive += 1
        if (y-1 >= 0):
            if (matrix[x][y-1].life == 1):
                neighbours_alive += 1

        if (y+1 <= 19):
            if (matrix[x][y+1].life == 1):
                    neighbours_alive += 1
        return neighbours_alive

    def update(self, life, neighbours_alive):
        if (life==0):
            if (neighbours_alive==3):
                life=1
        else:
            if (neighbours_alive==2 or neighbours_alive==3):
                life=1
            else:
                life=0
        return life
