from Vector import Vector;
from RobotEnums import Direction, MachineState;

class Machine:
    __factoryBoundsMin = 0;
    __factoryBoundsMax = 1000;
    __maxPackageCount = 3;
    __startingPosition = Vector(0, 0);
    
    def ToString(self):
        return "Robot -> " + self.Position.ToString() + " | Moved " + str(len(self.MoveHistory)) + " times";
    
    def __init__(self):
        self.Position = Machine.__startingPosition;
        self.MoveHistory = [];
        self.MoveHistory.append(self.Position);
        self.Packages = [];
        self.State = MachineState.AT_HOME;
    
    def __CheckPosition(self, coordinate):
        if(coordinate.X < Machine.__factoryBoundsMin or coordinate.Y < Machine.__factoryBoundsMin or 
           coordinate.X > Machine.__factoryBoundsMax or coordinate.Y > Machine.__factoryBoundsMax):
            return False;
        return True;
    
    def Move(self, direction):
        newPosition = Vector(self.Position.X, self.Position.Y);
        
        match direction:
            case Direction.LEFT:
                newPosition.X -= 1;
            case Direction.UP:
                newPosition.Y += 1;
            case Direction.RIGHT:
                newPosition.X += 1;
            case Direction.DOWN:
                newPosition.Y -= 1;
                
        if(self.__CheckPosition(newPosition)):
            self.Position = newPosition;
            print(self.Position.ToString());
            self.MoveHistory.append(self.Position);
    
    def PickupPackage(self, package):
        if(self.State != MachineState.INVENTORY_FULL):
            if(package in self.Packages):
                raise Exception(package.ToString() + " is already in robot inventory. Can't pick up!");
            self.Packages.append(package);
            package.Pickup();
            print("Picked up package: " + package.ToString());
        
            if(len(self.Packages) == Machine.__maxPackageCount):
                self.State = MachineState.INVENTORY_FULL;
    
    def DeliverPackage(self, package):
        if(self.State != MachineState.WAITING_TO_HOME):
            if(package not in self.Packages):
                raise Exception(package.ToString() + " was not fount in robot inventory. Can't deliver!");
            self.Packages.remove(package);
            package.Deliver();
            print("Delivered package: " + package.ToString());
        
            if(len(self.Packages) == 0):
                self.State = MachineState.WAITING_TO_HOME;
    
    def ChooseDestination(self):
        if(len(self.Packages) < 1):
            if(self.Position == Machine.__startingPosition):
                self.State = MachineState.AT_HOME;
                return;
            else:
                self.Destination = Machine.__startingPosition;
        else:
            minDistanceLength = self.Position.DistanceFrom(self.Packages[0].Destination);
            minDistancePackage = self.Packages[0];
            for i in range(1, len(self.Packages)):
                currentDistance = self.Position.DistanceFrom(self.Packages[i].Destination);
                if(currentDistance < minDistanceLength):
                    minDistanceLength = currentDistance;
                    minDistancePackage = self.Packages[i];
            self.Destination = minDistancePackage.Destination;
            self.PackageBeingDelivered = minDistancePackage;
        
        self.State = MachineState.MOVING;
    
    def HandleMovement(self):
        destinationVector = self.Destination - self.Position;
        if(destinationVector.X > 0):
            self.Move(Direction.RIGHT);
        elif(destinationVector.X < 0):
            self.Move(Direction.LEFT);
        elif(destinationVector.Y > 0):
            self.Move(Direction.UP);
        elif(destinationVector.Y < 0):
            self.Move(Direction.DOWN);
        else:
            self.State = MachineState.REACHED_DESTINATION;
            print("Reached destination!")
            if(self.PackageBeingDelivered is not None):
                self.DeliverPackage(self.PackageBeingDelivered);
                self.PackageBeingDelivered = None;