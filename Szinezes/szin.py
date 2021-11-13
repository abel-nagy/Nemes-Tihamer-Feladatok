import os;
from collections import namedtuple;

#region Properties

folderPath = os.path.dirname(os.path.normpath(__file__));
inputFilePath = os.path.join(folderPath, "szin.be");
outputFilePath = os.path.join(folderPath, "szin.ki");

#endregion Properties

buildingHeight = 0;
indexOfRequiredColoring = 0;

#region Functions

def ReadFile():
    file = open(inputFilePath);
    
    global buildingHeight;
    global indexOfRequiredColoring;
    
    firstRow = file.readline().split();
    buildingHeight = int(firstRow[0]);
    indexOfRequiredColoring = int(firstRow[1]);
    
    file.close();

def Calculate():
    return;

def WriteFile():
    file = open(outputFilePath, "w");
    file.close();

#endregion Functions

#region Start

os.system('cls');

ReadFile();
Calculate();
WriteFile();

#endregion Start