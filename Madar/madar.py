import os;
from bird import Bird;

#region Properties
folderPath = os.path.dirname(os.path.normpath(__file__));
inputFilePath = os.path.join(folderPath, "madar.be");
outputFilePath = os.path.join(folderPath, "madar.ki");
birdCount = 0;
areaSize = 0;
birds = [];
fightingBirdsIds = [];
notFightingBirdsIds = [];
birdsWithFullyCoveredTerritoriesIds = [];
#endregion Properties

#region Functions

def CheckFileInput(row):
    if(birdCount < 1 or birdCount > 1000):
        raise Exception("Bird count must be within Range(1,1000)!");
    if(areaSize < 1 or areaSize > 10000):
        raise Exception("Area size must be within Range(1,10000)!");
    if(int(row[0]) < 1 or int(row[0]) > areaSize):
        raise Exception("Birds territory X must be within Range(1," + str(areaSize) + ")!");
    if(int(row[1]) < 1 or int(row[1]) > areaSize):
        raise Exception("Birds territory Y must be within Range(1," + str(areaSize) + ")!");
    if(int(row[2]) < 1 or int(row[2]) > 100):
        raise Exception("Territory Size must be within Range(1,100)!");

def ReadFile():
    file = open(inputFilePath);
    
    firstRow = file.readline().split();6
    
    global birdCount;
    global areaSize;
    birdCount = int(firstRow[0]);
    areaSize = int(firstRow[1]);
    
    global birds;
    for i in range(0, birdCount):
        currentRow = file.readline().split();
        
        try: CheckFileInput(currentRow);
        except Exception as exc: print(exc); return False;
        
        newBird = Bird( int(currentRow[0]), int(currentRow[1]), int(currentRow[2]) );
        birds.append(newBird);
    print();
    file.close();
    return True;

def AreTerritoriesOverlapping(a, b):
    # If one rectangle is on left side of other
    if(a.UpperLeft.X > b.LowerRight.X or b.UpperLeft.X >= a.LowerRight.X):
        return False
 
    # If one rectangle is above other
    if(a.UpperLeft.Y > b.LowerRight.Y or b.UpperLeft.Y > a.LowerRight.Y):
        return False
 
    return True

def DoesTerritoryFullyContainOther(a, b):
    xContains = False;
    yContains = False;
    
    if((a.UpperLeft.X <= b.UpperLeft.X and a.LowerRight.X >= b.LowerRight.X)):
        xContains = True;
 
    if((a.UpperLeft.Y <= b.UpperLeft.Y and a.LowerRight.Y >= b.LowerRight.Y)):
        yContains = True;
 
    return xContains and yContains;

def Calculate():
    for i in range(0, birdCount):
        for j in range(0, birdCount):
            if(i == j):
                continue;
            
            if(birds[j].Id not in birds[i].RivalsIds):
                if(AreTerritoriesOverlapping(birds[i].Territory, birds[j].Territory)):
                    birds[i].RivalsIds.append(birds[j].Id);
                    birds[j].RivalsIds.append(birds[i].Id);
                    
                    if(birds[i].Id not in fightingBirdsIds):
                        fightingBirdsIds.append(birds[i].Id);
                    if(birds[j].Id not in fightingBirdsIds):
                        fightingBirdsIds.append(birds[j].Id);
                    
                    print(str(i) + " is fighting " + str(j) + " for a territory.");
                    if(DoesTerritoryFullyContainOther(birds[j].Territory, birds[i].Territory)):
                        birdsWithFullyCoveredTerritoriesIds.append(birds[i].Id);
                        print("\t And it's territory is fully covered by " + str(birds[j].Id) + ".");
            else:
                print(str(i) + " is fighting " + str(j) + " for a territory.");
                if(DoesTerritoryFullyContainOther(birds[j].Territory, birds[i].Territory)):
                    birdsWithFullyCoveredTerritoriesIds.append(birds[i].Id);
                    print("\t And it's territory is fully covered by " + str(birds[j].Id) + ".");
                    print();
        
        if(len(birds[i].RivalsIds) == 0):
            notFightingBirdsIds.append(birds[i].Id);
            print(str(i) + " isn't fighting any other birbs.");
        print();

def ChooseBiggestFighter(fightingBirdsIds):
    maxCount = 0;
    maxId = 0;
    
    for i in fightingBirdsIds:
        if(len(birds[i].RivalsIds) > maxCount):
            maxCount = len(birds[i].RivalsIds);
            maxId = i;
    return maxId + 1;

def WriteFile():
    file = open(outputFilePath, "w");
    
    for birb in notFightingBirdsIds:
        file.write(str(birb+1) + " ");
    file.write("\n");
    
    file.write(str(ChooseBiggestFighter(fightingBirdsIds)) + "\n");
    
    for birb in birdsWithFullyCoveredTerritoriesIds:
        file.write(str(birb+1) + " ");
    file.write("\n");
    
    file.close();

#endregion Functions

#region Start

os.system('cls');

if(ReadFile()):
    Calculate();
    WriteFile();

#endregion Start