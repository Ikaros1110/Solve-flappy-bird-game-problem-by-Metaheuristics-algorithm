import random as rm
class solutionRepresent:
    def __init__(self, solution = 0) -> None:
        if solution == 0:
            self.random_generate()
        else:
            self.solution = solution
    

    def random_generate(self)-> None:
        newSolution = list()
        newSolution.append(rm.randint(0,512))  # bird Y point
        newSolution.append((rm.randint(-1000,800))/100) # bird speed
        newSolution.append(rm.randint(0,288)) # pipe X point
        yPair = list()
        yPair.append(rm.randint(180,320))
        yPair.append(rm.randint(yPair[0],320))
        newSolution.append(yPair)
        if rm.randint(0,1) == 1:
            newSolution.append(True)
        else:
            newSolution.append(False)
        self.solution = newSolution

    def print(self)-> None:
        for e in self.solution:
            print(e)