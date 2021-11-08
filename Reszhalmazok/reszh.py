import os;
from collections import namedtuple;
from student import Student;

#region Properties

folderPath = os.path.dirname(os.path.normpath(__file__));
inputFilePath = os.path.join(folderPath, "reszh.be");
outputFilePath = os.path.join(folderPath, "reszh.ki");

students = [];
scflList = [];
scfsList = [];

scfl = namedtuple("SCFL", ["LanguageID", "StudentCount"]);
scfs = namedtuple("SCFS", ["SportID", "StudentCount"]);
#endregion Properties

#region Functions

def ReadFile():
    file = open(inputFilePath);
    
    firstRow = file.readline().split();
    
    studentCount = int(firstRow[0]);
    languageCount = int(firstRow[1]);
    sportCount = int(firstRow[2]);
    
    # Create empty tuples
    studentsLanguageInOrder = [];
    studentsSportInOrder = [];
    # Fill up tuples to be fixed sized
    for i in range(0, studentCount):
        studentsLanguageInOrder.append(0);
    for i in range(0, studentCount):
        studentsSportInOrder.append(0);
    
    # Fill up language tuple with actual data
    for i in range(0, languageCount):
        currentLine = file.readline().split();
        
        global scflList;
        scflList.append(scfl(i + 1, int(currentLine[0])));
        
        currentLine.pop(0);
        for j in currentLine:
            studentsLanguageInOrder[int(j) - 1] = i + 1;
    
    # Fill up sport tuple with actual data
    for i in range(0, sportCount):
        currentLine = file.readline().split();
        
        global scfsList;
        scfsList.append(scfs(i + 1, int(currentLine[0])));
        
        currentLine.pop(0);
        for j in currentLine:
            studentsSportInOrder[int(j) - 1] = i + 1;
    
    global students;
    
    # Create Student objects with associated Language and Sport ids
    for i in range(0, studentCount):
        currentStudent = Student(i, studentsLanguageInOrder[i], studentsSportInOrder[i]);
        students.append(currentStudent);
    
    file.close();

def Calculate():
    global finalResult;
    finalResult = 0;
    checkedSportIds = [];
    languageThingies = [];
    
    for i in range(0, len(students)):
        if students[i].SportId in checkedSportIds:
            continue;
        
        associatedSportStats = [scfs(sport.SportID, sport.StudentCount) for sport 
                                in scfsList if sport.SportID == students[i].SportId];
        if(students[i].SportId == associatedSportStats[0].SportID and associatedSportStats[0].StudentCount == 1):
            if(students[j].LanguageId not in languageThingies):
                languageThingies.append(students[j].LanguageId);
            continue;
                
        counter = 1;
        for j in range(i + 1, len(students)):
            if(students[j].SportId == students[i].SportId and students[j].LanguageId == students[i].LanguageId):
                counter += 1;
        
        if(associatedSportStats[0].StudentCount == counter and students[i].LanguageId not in languageThingies):
            languageThingies.append(students[i].LanguageId);
        
        checkedSportIds.append(students[i].SportId);
    
    finalResult = len(languageThingies);

def WriteFile():
    file = open(outputFilePath, "w");
    file.write(str(finalResult));
    file.close();
    print(finalResult);

#endregion Functions

#region Start

os.system('cls');

ReadFile();
Calculate();
WriteFile();

#endregion Start