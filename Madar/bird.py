
class Coordinate:
    def __init__(self, x, y):
        self.X = int(x);
        self.Y = int(y);
    
    def ToString(self):
        return "[" + str(self.X) + "," + str(self.Y) + "]";

class Territory:    
    def __init__(self, territoryX, territoryY, territorySize):
        self.Size = territorySize;
        self.UpperLeft = Coordinate(territoryX - territorySize, territoryY - territorySize);
        self.LowerRight = Coordinate(territoryX + territorySize, territoryY + territorySize);
    
    def ToString(self):
        return "(" + self.UpperLeft.ToString() + " " + self.LowerRight.ToString() + ")";

class Bird:
    idCounter = 0;
    
    def PutTogether(self, coordinate):
        return "[" + str(coordinate.X) + "," + str(coordinate.Y) + "]";
    
    def DisplayTerritoryNumbers(self):
        print(str(self.Id) + " (s" + str(self.Territory.Size) + "): " + 
              self.PutTogether(self.Territory.UpperLeft) + " " + 
              self.PutTogether(self.Territory.LowerRight))
    
    def __init__(self, territoryX, territoryY, territorySize):
        self.Id = Bird.idCounter;
        self.Territory = Territory(territoryX, territoryY, territorySize);
        self.RivalsIds = [];
        Bird.idCounter += 1;
        self.DisplayTerritoryNumbers();