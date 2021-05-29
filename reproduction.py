import random as rm

class Reproduction:
    
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        
    def random_switch_half(self):
        datasize = len(self.father)
        samePart = rm.sample(list(i for i in range(datasize)), datasize//2)
        son = list()
        daughter = list()
        for e in range(datasize):
            if (e in samePart):
                son.append(self.father[e])
                daughter.append(self.mother[e])
            else:
                son.append(self.mother[e])
                daughter.append(self.father[e])
        return son, daughter
        #self.father = son
        #self.mother = daughter