from cache import Cache
class MOESI(object):
    def __init__(self):
        pass
        
    def readFile(self, filePath):
        lineList = []
        with open(filePath,'r') as f:
            for line in f:
                lineList.append(line)
        return lineList
	
    def process(self, lineList):
        cacheNumber, cacheFunction, lineNumber = 0, "", 0
        c = [Cache() for i in range(3)]
        count = 0
        for line in lineList:
            count = count + 1
            print line.strip()
            cacheNumber = int(line[0])
            cacheFunction = line[1]
            lineNumber = int(line[2])
            
            if(cacheFunction == 'w'):
                c[cacheNumber].procWrite(lineNumber, cacheNumber, c)
            elif(cacheFunction == 'r'):
                c[cacheNumber].procRead(lineNumber, cacheNumber, c) 
            elif(cacheFunction == 'e'):
                c[cacheNumber].procEvict(lineNumber, cacheNumber, c)
            print ""