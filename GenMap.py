class Map:

    def __init__(self, x, y):
        self.xdim = x
        self.ydim = y
        self.errorStr = "-1"
        self.filler = "-"

    def defineError(self, error):
        self.errorStr = error

    def defineFiller(self, fill):
        self.filler = fill

    def genArray(self):
        self.mapArr = [[self.filler] * self.ydim for i in range(self.xdim)]

    def printMap(self):
        mapString = ""
        
        for y in range(0, self.ydim):
            mapString += "\n"
            
            for x in range(0, self.xdim):
                mapString += self.mapArr[x][y] 
                mapString += " "
        
        print(mapString, end="")
        
    def getCharAtIndex(self, x, y):
        
        if(x >= self.xdim or x < 0 or y >= self.ydim or y < 0):
            return self.errorStr
        
        return self.mapArr[x][y]
        
    def setCharAtIndex(self, x, y, value):
        
        if(x >= self.xdim or x < 0 or y >= self.ydim or y < 0):
            return self.errorStr
        
        self.mapArr[x][y] = value
        
    