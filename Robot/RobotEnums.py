from enum import Enum;

class Direction(Enum):
    LEFT = 0;
    UP = 1;
    RIGHT = 2;
    DOWN = 3;    

class PackageState(Enum):
    OnConveyorBelt = 0;
    WaitingForDelivery = 1;
    PickedUp = 2;
    Delivered = 3;

class MachineState(Enum):
    AT_HOME = 0;
    INVENTORY_FULL = 1;
    MOVING = 2;
    WAITING_TO_HOME = 3;
    REACHED_DESTINATION = 4;