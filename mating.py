import numpy as np

from random import sample

class mating:

    __pairSets = []

    #data: dataSets, score: targetValue of data with same order
    def __call__(self, data, score):
        #tournament selection
        n = len(score)

        for _ in range(n):
            pair = []
            while len(pair) < 2:
                randIndex = sample(range(len(score)), 2)
                if score[randIndex[0]] >= score[randIndex[1]]: pair.append(data[randIndex[0]])
                else: pair.append(data[randIndex[1]])
            self.__pairSets.append(pair)
        return self.__pairSets
    
    def test(self, data=[[1,2],[3,4],[5,6],[7,8]], score=[0,1,2,3]):
        try:
            print("Try \"__call__\" function is working...")
            self(data, score)
        except:
            print("Error: \"__call__\" function can't work")
        print("Test done")
