import sys
class Tournament(object):
    historyBits = '000000'
    
    #method to read File
    @staticmethod
    def readFile(filePath):
        lineList = []
        with open(filePath,'r') as f:
            for line in f:
                lineList.append(line)
        return lineList

    #Local Prediction
    @staticmethod
    def calcLocalPrediction(branch, localPredictor, line):
        index = int(line[0])
        localPrediction = ''
        old = localPredictor[index]
        if(localPredictor[index] < 2):
            localPrediction = 'n'
        elif(localPredictor[index] >= 2):
            localPrediction = 't'
        if(localPredictor[index] >= 0 and branch == 'n'):
            if(localPredictor[index] != 0):
                localPredictor[index] = localPredictor[index] - 1
        elif(localPredictor[index] <= 3 and branch == 't'):
            if(localPredictor[index] != 3):
                localPredictor[index] = localPredictor[index] + 1
        new = localPredictor[index]
        return localPrediction, index, old, new

    #Global Prediction
    @staticmethod
    def calcGlobalPrediction(branch, globalPredictor, line):
        globalPrediction = ''
        tempHistory = Tournament.historyBits
        index = int('0b' + tempHistory, 2)
        old = globalPredictor[index]
        if(globalPredictor[index] < 2):
            globalPrediction = 'n'
        elif(globalPredictor[index] >= 2):
            globalPrediction = 't'
        
        if(globalPredictor[index] >= 0 and branch == 'n'):
            if(globalPredictor[index] != 0):
                globalPredictor[index] = globalPredictor[index] - 1
        elif(globalPredictor[index] <= 3 and branch == 't'):
            if(globalPredictor[index] != 3):
                globalPredictor[index] = globalPredictor[index] + 1

        tempHistory = tempHistory[1:]
        if(branch == 't'):
            tempHistory = tempHistory + '1'
        elif(branch == 'n'):
            tempHistory = tempHistory + '0'
        Tournament.historyBits = tempHistory
        new = globalPredictor[index]
        return globalPrediction, index, old, new

    #Selector Prediction
    @staticmethod
    def calcSelectorPrediction(branch, selector, line, localValue, globalValue):
        index = int(line[0])
        selectorPrediction = ''
        old = selector[index]

        if(selector[index] < 2):
            selectorPrediction = 'l'
        elif(selector[index] >= 2):
            selectorPrediction = 'g'
       
        if(localValue == branch and globalValue != branch):
            if(selector[index] != 0):
                selector[index] = selector[index] - 1
        elif(localValue != branch and globalValue == branch):
            if(selector[index] != 3):
                selector[index] = selector[index] + 1

        new = selector[index]
        return selectorPrediction, index, old, new

    #Tournament Predictor
    @staticmethod
    def calcTournamentPrediction(localValue, globalValue, selectorValue):
        tournamentPrediction = ''
        if(selectorValue == 'l'):
            tournamentPrediction = localValue
        elif(selectorValue == 'g'):
            tournamentPrediction = globalValue
        return tournamentPrediction

    #Predict Method
    @staticmethod   
    def predict(lineList, localPredictor, globalPredictor, selector):
        l, g, t = 0, 0, 0
        results = []
        branch = ""
        localValue, globalValue = "", ""
        count = 0
        for line in lineList:
            if 'n' in line:
                branch = 'n'
            else:
                branch = 't'
            localValue, localI, localO, localN = Tournament.calcLocalPrediction(branch, localPredictor, line)
            globalValue, globalI, globalO, globalN = Tournament.calcGlobalPrediction(branch, globalPredictor, line)
            selectorValue, selectorI, selectorO, selectorN = Tournament.calcSelectorPrediction(branch, selector, line, localValue, globalValue)
            tournamentValue = Tournament.calcTournamentPrediction(localValue, globalValue, selectorValue)
            results.append(line[0] + localValue +  globalValue +  selectorValue + tournamentValue + branch)
            count = count + 1
        return results

'''main method'''
def main(args):
    
    localPredictor = [] #10
    globalPredictor = [] #64
    selector = [] #10
    
    localPredictor = [0] * 10
    globalPredictor = [0] * 64
    selector = [0] * 10
    
    if(len(sys.argv) != 3):
        print "Enter correct number of arguments"
        sys.exit()
    
    filePath = sys.argv[1]
    outputFilePath = sys.argv[2]
    lineList = Tournament.readFile(filePath)
    results = Tournament.predict(lineList, localPredictor, globalPredictor, selector)
    target = open(sys.argv[2], "w")
    for record in results:
        target.write(record + "\n")


''' If run as script, execute main '''
if __name__ == '__main__':
    main(sys.argv)
