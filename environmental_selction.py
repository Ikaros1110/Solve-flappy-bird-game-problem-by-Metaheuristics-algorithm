import numpy as np

class environmentalSelction:

    def __init__(self, parents, childs)-> None:
        self.parents = parents
        self.childs = childs
        self.groupSize = len(parents)

    def NN(self):
        sortParents = sorted(self.parents, key= lambda solutionRepresent:solutionRepresent.result, reverse=True)
        sortChilds = sorted(self.childs, key= lambda solutionRepresent:solutionRepresent.result, reverse=True)
        newGroup = []
        for e in range(self.groupSize//2):
            newGroup.append(sortParents[e])
            newGroup.append(sortChilds[e])
        return newGroup
    
