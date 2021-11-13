import os;

#region Properties

folderPath = os.path.dirname(os.path.normpath(__file__));
inputFilePath = os.path.join(folderPath, "madar.be");
outputFilePath = os.path.join(folderPath, "madar.ki");

#endregion Properties

#region Functions

def ReadFile():
    file = open(inputFilePath);
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