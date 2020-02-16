from GenMap import Map

from os import name, system
from time import sleep

import random

mapX = 75          #width of the map in terms of chars
mapY = 33          #height of the map in terms of chars
initNum = 300      #number of initial alive cells that are randomly placed
clearDelay = 1/15  #how long each generation is visualized before being cleared

class gameOfLife:
    def __init__(self, startingNum, map):
        self.initNum = startingNum
        self.myMap = map
        self.aliveChar = "o"        #char to visualize alive cell
        self.fillerChar = "-"       #char to visualize dead cell
        self.deadPlaceholder = "d"  #make sure this value is different from fillerChar
        self.alivePlaceholder = "a" #make sure this value is different from aliveChar

    def initMap(self):
        self.xlim = self.myMap.xdim
        self.ylim = self.myMap.ydim

        for i in range(0, self.initNum):
            x = random.randint(0, self.xlim - 1)
            y = random.randint(0, self.ylim - 1)

            if self.myMap.mapArr[x][y] == self.aliveChar:
                i += -1
            
            else:
                self.myMap.mapArr[x][y] = self.aliveChar

    def updateMap(self):
        for x in range(0, self.xlim):
            for y in range(0, self.ylim):
                surr = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
                
                count = 0
                #calculate number of neighbors that are alive
                for i in range(0, 8):
                    coor = surr[i]
                    deltax = x + coor[0]
                    deltay = y + coor[1]

                    curr = self.myMap.getCharAtIndex(deltax, deltay)

                    if(curr == self.aliveChar or curr == self.deadPlaceholder):
                        count += 1
                #insert placeholder based on number of neighbors
                if self.myMap.getCharAtIndex(x, y) == self.aliveChar:
                    
                    if count < 2:
                        self.myMap.setCharAtIndex(x, y, self.deadPlaceholder)

                    elif count == 2 or count == 3:
                        continue

                    elif count > 3:
                        self.myMap.setCharAtIndex(x, y, self.deadPlaceholder)
                
                elif count == 3:
                    self.myMap.setCharAtIndex(x, y, self.alivePlaceholder)

        #replace placeholders with actual chars
        for x in range(0, self.xlim):
            for y in range(0, self.ylim):
                
                if self.myMap.getCharAtIndex(x, y) == "d":
                    self.myMap.setCharAtIndex(x, y, self.fillerChar)

                elif self.myMap.getCharAtIndex(x, y) == "a":
                    self.myMap.setCharAtIndex(x, y, self.aliveChar)
#function to clear terminal                    
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
#create map object and generate array for the map
map = Map(mapX, mapY) 
map.genArray()
#create gameOfLife object and place random alive cells
GOL = gameOfLife(initNum, map)
GOL.initMap()

clear()
#print out the visualization
while True:
    map.printMap()
    GOL.updateMap()
    sleep(clearDelay)
    clear()


#map.printMap()
exit()