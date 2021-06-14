import random as rm
from evalution import *
from mutation import *

class solutionRepresent:
    # data    [bird Y , bird speed, pipe X, pipe Y,  isFlap ]
    # type     int      float       int     int      boolen
    # range    0~512    %.2f -8~10  0~288   142~404  True / False
    
    def __init__(self, solution = 0, NONE = False) -> None:
        if NONE:
            self.solution = []
            self.result = None
        elif solution == 0:
            self.solution = self.random_generate()
            EVALUATE = evaluation()
            self.result = EVALUATE(self.solution)
        else:
            self.solution = solution
            EVALUATE = evaluation()
            self.result = EVALUATE(self.solution)
    
    def __str__(self) -> str:
        return str(self.solution)+' '+str(self.result)

    def get_solution(self):
        return list(self.solution)

    def get_result(self):
        return self.result

    def get_solution_size(self):
        return len(self.solution)

    def set_solution(self, solution):
        self.solution = solution
        EVALUATE = evaluation()
        self.result = EVALUATE(self.solution)

    @staticmethod
    def random_generate()-> list:
        newSolution = list()
        newSolution.append(rm.randint(0,512))  # bird Y point
        newSolution.append((rm.randint(-800,1000))/100) # bird speed
        newSolution.append(rm.randint(0,288)) # pipe X point
        newSolution.append(rm.randint(142,404)) # lower pipe Y point , gap size is 100
        # 142~404 base on origin getRandomPipe() 
        if rm.randint(0,1) == 1:
            newSolution.append(True)
        else:
            newSolution.append(False)
        return newSolution

    def self_evaluate(self):
        EVALUATE = evaluation()
        self.result = EVALUATE(self.solution)

    def change_self_flaped_solution(self):
        self.solution[-1] = not self.solution[-1]
        self.self_evaluate()

    def get_change_flaped_solution(self):
        newSolution =  list(self.solution)
        newSolution[-1] = not newSolution[-1]
        return newSolution

    def set_better_flaped_choice(self):
        EVALUATE = evaluation()
        newResult = EVALUATE(self.get_change_flaped_solution())
        if newResult > self.result:
            self.change_self_flaped_solution()
            self.result = newResult

    def self_mutation(self):
        MUTATE = mutation()
        upperBound = [512, 18, 288, 404, 0]
        self.solution = MUTATE(self.solution, upperBound)
        self.solution[1] =  - 10 # mutation lowerbound is 0, so Shift right
        self.solution[3] =  -142 # mutation lowerbound is 0, so Shift right
        self.self_evaluate()

    def print(self, respective = False)-> None:
        if respective:
            for e in self.solution:
                print(e)
        else:
            print(self.solution)
    
    def write_to_file(self, fileName):
        f = open('result/'+fileName, 'a')
        writeData = list(self.get_solution())
        writeData[1] = self.solution[2]
        writeData[2] = self.solution[3]
        writeData[3] = self.solution[1]
        for e in writeData:
            f.write(str(e)+' ')
        f.write('\n')
        f.close()