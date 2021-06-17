import random as rm
import time
from solution_represent import solutionRepresent
from evalution import *
def writeFile(data, fileName, openMode = 'a'):
    f = open(fileName, openMode)
    f.write(data)
    f.close()

def readFile(fileName, openMode = 'r'):
    f = open(fileName, openMode)
    data = f.read()
    f.close()
    return data


def main(): # 200 500, 50 ,100
    numList = [20000, 40000, 50000, 100000]
    allTimes = 10
    version = 'Ver3_'
    for generateNum in numList:
        for RDTimes in range(allTimes):
            print("GenerateNum: ",generateNum,',times: ',RDTimes)
            fileName = version+ 'randomGenerate_' + str(generateNum) +'_'+str(RDTimes)  + '.txt'
            # startTime = time.time()
            for _ in range(generateNum):
                newSolution = solutionRepresent()
                newSolution.set_better_flaped_choice()
                newSolution.write_to_file(fileName)
            print('OK')      

if __name__ == '__main__':
    main()