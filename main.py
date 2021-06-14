from solution_represent import solutionRepresent
from mating import mating
from reproduction import Reproduction
from environmental_selction import environmentalSelction
def pair_combination(peoplePair, size):
    people = []
    for i in range(size):
        people.append(peoplePair[i][0])
        people.append(peoplePair[i][1])
    return people

def main():
    ### set parameter ###
    groupSize = 20
    generateTimes = 10
    print("Size: ",groupSize,"Times: ",generateTimes)
    ### initilze group ###
    group = []
    for _ in range(groupSize):
        group.append(solutionRepresent())
    ### run GA ###
    for _ in range(generateTimes):
        groupResult = []
        for e in group:
            groupResult.append(e.get_result())
        MATING = mating()
        parentsPair = MATING(group, groupResult)
        parents = pair_combination(parentsPair, groupSize)
        childs = []
        for i in range(groupSize//2):
            parentREPRODUCT = Reproduction(parentsPair[i][0], parentsPair[i][1])
            newChildPair = parentREPRODUCT.random_switch_half()
            # newChildPair[0].self_mutation()
            # newChildPair[1].self_mutation()
            childs.append(newChildPair[0])
            childs.append(newChildPair[1])
        ES = environmentalSelction(parents, childs)
        group = ES.NN()
        for e in group:
            fileName = 'GA_'+str(groupSize)+'_'+str(generateTimes)+'.txt'
            e.set_better_flaped_choice()
            e.write_to_file(fileName)
    print('OK')

    
if __name__ == '__main__':
    main()