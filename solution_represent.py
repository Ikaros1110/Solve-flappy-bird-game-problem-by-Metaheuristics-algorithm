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
        pipePair1 = list()
        pipePair2 = list() #pipi point
        pipePair1.append(rm.randint(0,288))
        pipePair1.append(rm.randint(180,320))
        pipePair2.append(rm.randint(pipePair1[0],288))
        pipePair2.append(rm.randint(pipePair1[1],320))
        newSolution.append(pipePair1)
        newSolution.append(pipePair2)
        if rm.randint(0,1) == 1:
            newSolution.append(True)
        else:
            newSolution.append(False)
        self.solution = newSolution

    def print(self):
        for e in self.solution:
            print(e)