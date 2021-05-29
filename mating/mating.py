import numpy as np

from random import sample

def mating(data, score):
    #tournament selection
    pairSets = []
    n = len(score)

    for i in range(n):
        pair = []
        while len(pair) < 2:
            randIndex = sample(range(len(score)), 2)
            if score[randIndex[0]] >= score[randIndex[1]]: pair.append(data[randIndex[0]])
            else: pair.append(data[randIndex[1]])
        pairSets.append(pair)
    return pairSets