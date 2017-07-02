import sys
from line import Line
class Cache(object):
    line = []
    def __init__(self):
        self.line = [Line() for i in range(4)]

    def procRead(self, lineNumber, cacheNumber, c):
        if(c[cacheNumber].line[lineNumber].hit == 0):
            print "Cache " + str(cacheNumber) + ", Miss " + str(lineNumber)
            print ""
            temp = []
            for i in range(3):
                if cacheNumber != i:
                    value = c[i].busRead(lineNumber, i, c)
                    temp.append(value)
                    if(value == 1):
                    	break;
                    
            
            if 1 not in temp:
                previousState = c[cacheNumber].line[lineNumber].state
                c[cacheNumber].line[lineNumber].state = "E"
                currentState = c[cacheNumber].line[lineNumber].state
                print "Cache " + str(cacheNumber)
                
                if(previousState == "I" and currentState == "E"):
                    print "Memory Read"
                    c[cacheNumber].line[lineNumber].hit = 1
                print previousState, "->", currentState

            else:
                previousState = c[cacheNumber].line[lineNumber].state
                c[cacheNumber].line[lineNumber].state = "S"
                currentState = c[cacheNumber].line[lineNumber].state
                c[cacheNumber].line[lineNumber].hit = 1
                print previousState, "->", currentState 

        elif(c[cacheNumber].line[lineNumber].hit == 1):
            previousState = c[cacheNumber].line[lineNumber].state
            if previousState == "M" or previousState == "O":
                print "Cache " + str(cacheNumber) + ", Hit Dirty " + str(lineNumber)
            else:
                print "Cache " + str(cacheNumber) + ", Hit " + str(lineNumber)
            
            if(c[cacheNumber].line[lineNumber].state == "O"):
                pass
            elif(c[cacheNumber].line[lineNumber].state == "E"):
                pass

            currentState = c[cacheNumber].line[lineNumber].state
            print previousState, "->", currentState

    def procWrite(self, lineNumber, cacheNumber, c):
        if(c[cacheNumber].line[lineNumber].hit == 0):
            print "Cache " + str(cacheNumber) + ", Miss " + str(lineNumber)
            temp = []
            for i in range(3):
                if cacheNumber != i:
                    value = c[i].busWrite(lineNumber, i, c)
                    temp.append(value)
            
            if 1 not in temp:
                pass

            else:
                previousState = c[cacheNumber].line[lineNumber].state
                for i in range(3):
                    if cacheNumber != i:
                        c[i].line[lineNumber].state = "I"
                        c[i].line[lineNumber].hit = 0
                    else:
                        c[i].line[lineNumber].state = "M"
                        c[i].line[lineNumber].hit = 1
                        currentState = c[i].line[lineNumber].state
                
                print previousState, "->", currentState
        elif(c[cacheNumber].line[lineNumber].hit == 1):
            previousState = c[cacheNumber].line[lineNumber].state
            if previousState == "M" or previousState == "O" :
                print "Cache " + str(cacheNumber) + ", Hit Dirty " + str(lineNumber)
            else:
                print "Cache " + str(cacheNumber) + ", Hit " + str(lineNumber)
            if(previousState == "E"):
                c[cacheNumber].line[lineNumber].state = "M"
            elif(previousState == "M"):
                pass
            
            temp = []
            for i in range(3):
                if cacheNumber != i:
                    value = c[i].busWrite(lineNumber, i, c)
                    temp.append(value)
            
            if 1 not in temp:
                pass

            else:
                previousState = c[cacheNumber].line[lineNumber].state
                for i in range(3):
                    if cacheNumber != i:
                        c[i].line[lineNumber].state = "I"
                        c[i].line[lineNumber].hit = 0
                    else:
                        c[i].line[lineNumber].state = "M"
                        c[i].line[lineNumber].hit = 1
                        currentState = c[i].line[lineNumber].state
            currentState = c[cacheNumber].line[lineNumber].state
            print previousState, "->", currentState

    def busRead(self, lineNumber, cacheNumber, c):
        print "Cache " + str(cacheNumber) + ", Bus Read " + str(lineNumber)
        if(c[cacheNumber].line[lineNumber].hit == 0):
            print "Miss"
            if(c[cacheNumber].line[lineNumber].state == "I"):
                print c[cacheNumber].line[lineNumber].state, "->", c[cacheNumber].line[lineNumber].state
            print "End Bus Read"
            print ""
            return 0
        elif(c[cacheNumber].line[lineNumber].hit == 1):
            if(c[cacheNumber].line[lineNumber].state == "M" or c[cacheNumber].line[lineNumber].state == "O"):
                print "Hit Dirty"
            else:
                print "Hit"
            previousState = c[cacheNumber].line[lineNumber].state
            currentState = previousState
            if(previousState == "E"):
                c[cacheNumber].line[lineNumber].state = "S"
                currentState = c[cacheNumber].line[lineNumber].state
            elif(previousState == "M" or previousState == "O"):
                c[cacheNumber].line[lineNumber].state = "O"
                currentState = c[cacheNumber].line[lineNumber].state
            print previousState, "->", currentState
            print "End Bus Read"
            print ""
            return 1

    def busWrite(self, lineNumber, cacheNumber, c):
        print ""
        print "Cache " + str(cacheNumber) + ", Bus Write " + str(lineNumber)
        if(c[cacheNumber].line[lineNumber].hit == 0):
            print "Miss"
            previousState = c[cacheNumber].line[lineNumber].state
            c[cacheNumber].line[lineNumber].state = "I"
            currentState = c[cacheNumber].line[lineNumber].state
            print previousState, "->", currentState
            print "End Bus Write"
            print ""
            return 0
        elif(c[cacheNumber].line[lineNumber].hit == 1):
            if(c[cacheNumber].line[lineNumber].state == "M" or c[cacheNumber].line[lineNumber].state == "O"):
                print "Hit Dirty"
            else:
                print "Hit"
            print "Flush"
            previousState = c[cacheNumber].line[lineNumber].state
            c[cacheNumber].line[lineNumber].state = "I"
            currentState = c[cacheNumber].line[lineNumber].state
            print previousState, "->", currentState
            print "End Bus Write"
            print ""
            return 1

    def procEvict(self, lineNumber, cacheNumber, c):
        previousState = c[cacheNumber].line[lineNumber].state
        if(previousState == "O"):
            print "Memory Update"
        
        print "Flush"
        c[cacheNumber].line[lineNumber].state = "I"
        c[cacheNumber].line[lineNumber].hit = 0
        currentState = c[cacheNumber].line[lineNumber].state
        print previousState, "->", currentState
