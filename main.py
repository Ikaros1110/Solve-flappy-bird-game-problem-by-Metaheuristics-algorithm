from solution_represent import solutionRepresent
from mating import mating
from reproduction import Reproduction
def main():
    ### set parameter ###
    groupSize = 20
    generateTimes = 1
    ### initilze group ###
    group = []
    for _ in range(groupSize):
        group.append(solutionRepresent())
    groupResult = []
    for e in group:
        groupResult.append(e.get_result())
    ### run GA ###
    for _ in range(generateTimes):
        MATING = mating()
        parentPair = MATING(group, groupResult)
        for i in range(groupSize//2):
            REPRODUCT = Reproduction(parentPair[i][0], parentPair[i][1])
            newChildPair = REPRODUCT.random_switch_half()
            newChildPair[0].self_mutation()
            newChildPair[1].self_mutation()
        



    
if __name__ == '__main__':
    main()