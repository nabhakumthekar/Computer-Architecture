import sys
class Line(object):
    state = "" # line status
    hit = 0 # line hit or miss

    def __init__(self):
        self.state = "I"
        self.hit = 0

    def setState(self):
        print "Set State"    

    def getState(self):
        print "Get State"    

    def setHit(self):
        print "Set Hit"

    def getHit(self):
        print "Get Hit"