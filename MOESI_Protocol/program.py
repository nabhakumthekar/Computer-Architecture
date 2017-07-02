import sys
from cache import Cache
from moesi import MOESI    
'''main method'''
def main(args):
    filePath = raw_input('')
    
    m = MOESI()
    lineList = m.readFile(filePath)
    m.process(lineList)
    
''' If run as script, execute main '''
if __name__ == '__main__':
    main(sys.argv)