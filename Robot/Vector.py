import math;

class Vector:
    def __init__(self, x, y):
        self.X = int(x);
        self.Y = int(y);
        self.Length = self.X + self.Y;
    
    def ToString(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")";
    
    def __add__(self, other):
        return Vector(self.X + other.X, self.Y + other.Y);
    
    def __sub__(self, other):
        return Vector(self.X - other.X, self.Y - other.Y);
    
    def __eq__(self, other):
        if(self.X == other.X and self.Y == other.Y):
            return True;
        else:
            return False;
    
    def DistanceFrom(self, other):
        differenceVector = other - self;
        return differenceVector.Length;