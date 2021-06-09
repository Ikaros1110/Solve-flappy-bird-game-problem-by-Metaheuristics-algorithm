import random as rm
class solutionRepresent:
    # data    [bird Y , bird speed, pipe X, pipe Y,  isFlap ]
    # type     int      float       int     int      boolen
    # range    0~512    %.2f -10~8  0~288   142~404  True / False
    
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
        newSolution.append(rm.randint(142,404)) # lower pipe Y point , gap size is 100
        # 142~404 base on origin getRandomPipe() 
        if rm.randint(0,1) == 1:
            newSolution.append(True)
        else:
            newSolution.append(False)
        self.solution = newSolution

    def print(self)-> None:
        for e in self.solution:
            print(e)