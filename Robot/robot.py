import os;

#region Properties
folderPath = os.path.dirname(os.path.normpath(__file__));
inputFilePath = os.path.join(folderPath, "robot.be");
outputFilePath = os.path.join(folderPath, "robot.ki");
#endregion Properties

#region Functions

def CheckFileInput(row):
    return;

def ReadFile():
    file = open(inputFilePath);
    
    file.close();
    return True;

def Calculate():
    return;

def WriteFile():
    file = open(outputFilePath, "w");
    file.close();

#endregion Functions

#region Start

os.system('cls');

if(ReadFile()):
    Calculate();
    WriteFile();

#endregion Start