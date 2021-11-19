import os;
from Package import Package;
from Machine import Machine;
from RobotEnums import Direction, MachineState, PackageState;

#region Properties
FolderPath = os.path.dirname(os.path.normpath(__file__));
InputFilePath = os.path.join(FolderPath, "robot.be");
OutputFilePath = os.path.join(FolderPath, "robot.ki");

PackageCount = 0;
Packages = [];
PackagesLeftToDeliverCount = 0;
#endregion Properties

#region Functions

def CheckPackageCoordinates(id, line):
    x = int(line[0]);
    if(x < 1 or x > 1000):
        raise Exception("X coordinate for Package[" + str(id) + "] was " + str(x) + " but it must be within Range(1,1000)");
    
    y = int(line[1]);
    if(y < 1 or y > 1000):
        raise Exception("Y coordinate for Package[" + str(id) + "] was " + str(y) + " but it must be within Range(1,1000)");

def ReadFile():
    file = open(InputFilePath);
    
    global PackageCount;
    global PackagesLeftToDeliverCount;
    PackageCount = int(file.readline());
    if(PackageCount < 1 or PackageCount > 10000):
        print("Package count must be within Range(1,10000)!");
        return False;
    PackagesLeftToDeliverCount = PackageCount;
    
    global packages;
    for i in range(0, PackageCount):
        currentLine = file.readline().split();
        
        try: CheckPackageCoordinates(i, currentLine);
        except Exception as exc: print(exc); return False;
        
        currentPackage = Package(int(currentLine[0]), int(currentLine[1]), i);
        Packages.append(currentPackage);
    
    file.close();
    return True;

def Calculate():
    global machine;
    machine = Machine();
    nextPackageInQueueId = 0;
    global PackagesLeftToDeliverCount;
    
    while(PackagesLeftToDeliverCount != 0):
        #print(machine.ToString());
        if(machine.State == MachineState.AT_HOME):
            machine.PickupPackage(Packages[nextPackageInQueueId]);
            nextPackageInQueueId += 1;
            isLastPlaceOnConveyorBeltOccupied = False;
            PackagesLeftToDeliverCount = 0;
            for package in Packages:
                isLastPlaceOnConveyorBeltOccupied = package.MoveUpOnBelt(isLastPlaceOnConveyorBeltOccupied) or isLastPlaceOnConveyorBeltOccupied;
                if(package.State != PackageState.Delivered):
                    PackagesLeftToDeliverCount += 1;
        elif(machine.State == MachineState.INVENTORY_FULL or machine.State == MachineState.REACHED_DESTINATION 
             or machine.State == MachineState.WAITING_TO_HOME):
            PackagesLeftToDeliverCount = 0;
            for package in Packages:
                if(package.State != PackageState.Delivered):
                    PackagesLeftToDeliverCount += 1;
            machine.ChooseDestination();
        elif(machine.State == MachineState.MOVING):
            machine.HandleMovement();
        
    print(len(machine.MoveHistory));

def WriteFile():
    file = open(OutputFilePath, "w");
    for pos in machine.MoveHistory:
        file.write(str(pos.X) + " " + str(pos.Y) + "\n");
    file.close();

#endregion Functions

#region Start

os.system('cls');

if(ReadFile()):
    Calculate();
    WriteFile();

#endregion Start