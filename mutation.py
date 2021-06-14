import numpy as np
import math
import random

class mutation:
    
    __newData = []

    @staticmethod
    def __sigmoid(x):
        return 1 / (1 + math.exp(-x))

    def __call__(self, data, upperBound):
        #data: data sets, upperBound: the data's upper value(lower default for 0)
        self.__newData = []
        for val, upper in zip(data, upperBound):
            if type(val)==bool: continue
            else:
                nd = self.__sigmoid(random.random()*2-1)#Do Normal distribution
                #origin in half place(0.5)
                diff = nd-0.5
                self.__newData.append(val+diff*(upper-val))
        self.__newData.append(data[-1])
        return self.__newData

    def test(self, data=[1,2,3,4,5], upperBound=[6,7,8,9,10]):
        try:
            print("Try \"__call__\" function is working...")
            self(data, upperBound)
        except:
            print("Error: \"__call__\" function can't work")

        print("Test done")

