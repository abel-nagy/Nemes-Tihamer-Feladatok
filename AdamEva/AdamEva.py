
from collections import namedtuple

#region Properties
Pair = namedtuple("Pair", ["Start", "End"])
inputFilePath = "adamEvaTestInput.txt";
resultsFilePath = "adamEvaTestResults.txt";
lastTime = 0;  # ?

adamTimes = [];
evaTimes = [];
resultTimes = [];
#endregion Properties

#region Helper Functions
def ReadTimes(file, times):
    periodCount = int(file.readline());
    for i in range(0, periodCount):
        line = file.readline().split();
        times.append( Pair(int(line[0]), int(line[1])) );

def DetermineStartTime(evaTime, adamTime):
    if(evaTime <= adamTime):
        return adamTime;
    else:
        return evaTime;
    
def DetermineEndTime(evaTime, adamTime):
    if(evaTime <= adamTime):
        return evaTime;
    else:
        return adamTime;
#endregion Helper Functions

#region Main Functions
def ReadFile():
    try:
        file = open(inputFilePath);
        
        global lastTime;
        lastTime = int( file.readline() );
        
        global adamTimes;
        ReadTimes(file, adamTimes)
        
        global evaTimes;
        ReadTimes(file, evaTimes);
        return True;
    except Exception as e:
        print("Something went wrong while trying to read input file!");
        print(e);
        return False;

def CalculateHours():
    for adamTime in adamTimes:
        for evaTime in evaTimes:
            resultStartHour = 0;
            resultEndHour = 0;
            
            if(evaTime.Start < adamTime.End and evaTime.End >= adamTime.Start):                
                resultStartHour = DetermineStartTime(evaTime.Start, adamTime.Start);
                resultEndHour = DetermineEndTime(evaTime.End, adamTime.End);
                resultTimes.append( Pair(resultStartHour, resultEndHour) );

def WriteResults():
    try:
        file = open(resultsFilePath, "w");
        
        file.write( str(len( resultTimes )) );
        print( str(len( resultTimes )) );
        for i in range(0, len( resultTimes )):
            print( str(resultTimes[i].Start) + " " + str(resultTimes[i].End) );
            file.write( "\n" + str(resultTimes[i].Start) + " " + str(resultTimes[i].End) );
        return True;
    except Exception as e:
        print("Something went wrong while trying to write to output file!");
        print(e);
        return False;

#endregion Main Functions

#region Main
if( ReadFile() ):
    CalculateHours();
    WriteResults();
#endregion Main