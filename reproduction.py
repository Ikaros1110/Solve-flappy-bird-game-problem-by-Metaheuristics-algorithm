import random as rm
from solution_represent import solutionRepresent

class Reproduction:

    def __init__(self, father, mother):
        self.father = father
        self.mother = mother

    def random_switch_half(self):
        datasize = self.father.get_solution_size()
        samePart = rm.sample(list(i for i in range(datasize)), datasize//2)
        son = list()
        daughter = list()
        for e in range(datasize):
            if (e in samePart):
                son.append(self.father.get_solution()[e])
                daughter.append(self.mother.get_solution()[e])
            else:
                son.append(self.mother.get_solution()[e])
                daughter.append(self.father.get_solution()[e])
        return [solutionRepresent(son),  solutionRepresent(daughter)]
