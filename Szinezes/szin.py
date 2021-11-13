import os, math;

#region Properties

folderPath = os.path.dirname(os.path.normpath(__file__));
inputFilePath = os.path.join(folderPath, "szin.be");
outputFilePath = os.path.join(folderPath, "szin.ki");

#endregion Properties

buildingHeight = 0;
indexOfRequiredColoring = 0;
validPaintingPatterns = [];

#region Functions

def ReadFile():
    file = open(inputFilePath);
    
    global buildingHeight;
    global indexOfRequiredColoring;
    
    firstRow = file.readline().split();
    buildingHeight = int(firstRow[0]) + 1;
    indexOfRequiredColoring = int(firstRow[1]);
    
    file.close();

def FillStartWithZeroes(input, fullLength):
    prefix = "";
    for i in range(0, fullLength - len(input)):
        prefix += "0";
    return prefix + input;

def CheckPaintingPatternValidity(paintingPattern):
    for i in range(0, len(paintingPattern) - 1):
        if(paintingPattern[i] == "1" and paintingPattern[i+1] == "1"):
            return False;
    return True;

def Calculate():
    global validPaintingPatterns;
    
    for i in range(0, int(math.pow(buildingHeight, 2))):
        numberInBinary = bin(i).replace("0b", "");
        if(len(numberInBinary) != buildingHeight):
            numberInBinary = FillStartWithZeroes(numberInBinary, buildingHeight);
        if(CheckPaintingPatternValidity(numberInBinary)):
            validPaintingPatterns.append(numberInBinary);

def WriteFile():
    file = open(outputFilePath, "w");
    
    file.write(str(len(validPaintingPatterns)) + "\n");
    print(str(len(validPaintingPatterns)));
    
    nextLine = "";
    for paint in validPaintingPatterns[indexOfRequiredColoring - 1]:
        nextLine += paint + " ";
        
    file.write(nextLine);
    print(nextLine);
    file.close();

#endregion Functions

#region Start

os.system('cls');

ReadFile();
Calculate();
WriteFile();

#endregion Start