import random as rm
from evalution import *
from mutation import *

class solutionRepresent:
    # data    [bird Y , bird speed, pipe X, pipe Y,  isFlap ]
    # type     int      float       int     int      boolen
    # range    0~512    %.2f -10~8  0~288   142~404  True / False
    
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
    
    def get_solution(self):
        return self.solution

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
        newSolution.append((rm.randint(-1000,800))/100) # bird speed
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

    def get_change_flaped_solution(self):
        newSolution =  self.solution
        newSolution[-1] = not newSolution[-1]
        return newSolution

    def set_better_flaped_choice(self):
        EVALUATE = evaluation()
        newResult = EVALUATE(self.get_change_flaped_solution())
        if newResult > self.result:
            self.change_self_flaped_solution()
            self.result = newResult

    def self_mutation(self):
        self.solution[0] = mutation(self.solution[0], 512)
        self.solution[1] = mutation(self.solution[1]+10, 18) - 10 # mutation lowerbound is 0, so Shift right
        self.solution[2] = mutation(self.solution[2], 288)
        self.solution[3] = mutation(self.solution[3]+142, 404) -142
        self.self_evaluate()

    def print(self, respective = False)-> None:
        if respective:
            for e in self.solution:
                print(e)
        else:
            print(self.solution)
    
    def write_to_file(self, fileName, append = True):
        openMode = 'a' if append else 'w'
        f = open('result/'+fileName, openMode)
        for e in self.solution:
            f.write(str(e)+' ')
        f.write('\n')
        f.close()