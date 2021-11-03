from collections import namedtuple;
PassengerIdPair = namedtuple("PassengerIdPair", ["id", "Passenger"])

class Passenger:
    idCounter = 0;
    PassengerList = [];
    
    def __init__(self, type, position, escalatorLength):
        self.id = Passenger.idCounter;
        self.type = type;
        self.position = position;
        self.escalatorLength = escalatorLength;
        Passenger.idCounter += 1;
        Passenger.PassengerList.append(PassengerIdPair(self.id, self));
    
    def Move(self):
        if(self.position == "escalatorDownX"):
            self.position = "escalatorDown0";
        elif(self.position.startswith("escalator")):
            escalatorPosition = int(self.position.replace("escalator", "").replace("Down", "").replace("Up", ""));
            if(escalatorPosition < self.escalatorLength - 1):
                self.position = self.position.replace(str(escalatorPosition), str(escalatorPosition+1));
            else:
                if(self.type.startswith("boarding")):
                    self.position = "lobby";
                elif(self.type.startswith("leaving")):
                    self.position = "left";
        elif(self.position.startswith("lobby")):
            if(self.type.startswith("boarding")):
                self.position = "metroOut";
            elif(self.type.startswith("leaving")):
                self.position = "escalatorUp0";
        elif(self.position.startswith("metroIn") and self.type.startswith("leaving")):
            self.position = "lobby";
    
    def GetPassengerById(idToLookFor):
        for id, passenger in Passenger.PassengerList:
            if(id == idToLookFor):
                return passenger;
    
    def GetPassengersByLocation(position):
        result = [];
        for passenger in Passenger.PassengerList:
            if(passenger.Passenger.position == position):
                result.append(passenger.Passenger);
        return result;