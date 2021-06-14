import random as rm
import time
from solution_represent import solutionRepresent
from evalution import *
def writeFile(data, fileName, openMode = 'a'):
    f = open(fileName, openMode)
    f.write(data)
    f.close()

def main():
    numList = [10000, 20000, 25000, 50000, 100000, 500000, 1000000]
    version = '_ver1'
    for generateNum in numList:
        print("GenerateNum: ",generateNum)
        fileName = 'randomGenarate/randomGenarate_' + str(generateNum) + version + '.txt'
        # startTime = time.time()
        for _ in range(generateNum):
            newSolution = solutionRepresent()
            newSolution.set_better_flaped_choice()
            newSolution.write_to_file(fileName)
        print('OK')            

if __name__ == '__main__':
    main()