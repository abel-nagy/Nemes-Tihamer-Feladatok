from Vector import Vector;
from RobotEnums import PackageState;

class Package:
    __idCounter = 0;
    
    def ToString(self):
        return "Package[" + str(self.ID) + "]" + self.Destination.ToString();
    
    def __init__(self, targetX, targetY, conveyorBeltPosition):
        self.ID = Package.__idCounter;
        Package.__idCounter += 1;
        self.Destination = Vector(targetX, targetY);
        self.ConveyorBeltPosition = conveyorBeltPosition;
        if(self.ConveyorBeltPosition == 0):
            self.State = PackageState.WaitingForDelivery;
        else:
            self.State = PackageState.OnConveyorBelt;
    
    def __eq__(self, other):
        if(self.ID == other.ID and self.Destination == other.Destination and self.State == other.State 
           and self.ConveyorBeltPosition == other.ConveyorBeltPosition):
            return True;
        else:
            return False;
    
    # Returns True if package moved to last position
    def MoveUpOnBelt(self, isLastPlaceOnConveyorBeltOccupied):
        if(self.State == PackageState.OnConveyorBelt):
            if(self.ConveyorBeltPosition == 1 and not isLastPlaceOnConveyorBeltOccupied):
                self.ConveyorBeltPosition -= 1;
                self.State = PackageState.WaitingForDelivery;
                return True;
            elif(self.ConveyorBeltPosition > 1):
                self.ConveyorBeltPosition -= 1;
            return False;
    
    def Pickup(self):
        if(self.State == PackageState.WaitingForDelivery):
            self.State = PackageState.PickedUp;
        else:
            raise Exception(self.ToString() + " isn't yet ready to be picked up!");
    
    def Deliver(self):
        if(self.State == PackageState.PickedUp):
            self.State = PackageState.Delivered;
        elif(self.State == PackageState.WaitingForDelivery):
            raise Exception(self.ToString() + " isn't yet ready to be delivered!");