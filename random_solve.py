import random as rm
import time
from solution_represent import solutionRepresent
from evalution import *

def main():
    generateNum = 500000
    fileName = 'randomGenarate_' + str(generateNum) + '.txt'
    startTime = time.time()
    for _ in range(generateNum):
        newSolution = solutionRepresent()
        newSolution.set_better_flaped_choice()
        newSolution.write_to_file(fileName, append=False)
    print("Use Time: ", time.time()-startTime)

if __name__ == '__main__':
    main()