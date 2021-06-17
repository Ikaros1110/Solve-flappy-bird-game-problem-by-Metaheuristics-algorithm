class solve:
    def __init__(self, fileName):
        self.__ans = False #default ans
        self.__lines = []
        with open(fileName) as f:
            for line in f.readlines():
                self.__lineParse(line.split())
        self.__lines.sort()

    def __call__(self, data):
        #binary search: O(logn)
        index = len(self.__lines)//2
        lower = 0
        upper = len(self.__lines)-1
        for i in range(len(self.__lines[0])-1):
            for j in range(1000):
                if data[i] > self.__lines[index][i]:
                    lower = index
                    index += (upper-index)//2
                elif data[i] < self.__lines[index][i]:
                    upper = index
                    index -= (index-lower)//2
                else: break
        # print(self.__lines[index]) # debug
        return self.__lines[index][4], [(0,0), (0,0)]

    def __lineParse(self, line):
        line[0] = int(line[0]) #bird Y
        line[1] = int(line[1]) #pipe X
        line[2] = int(line[2]) #pipe Y
        line[3] = float(line[3]) #bird Speed
        if line[4]=='True': line[4] = True
        else: line[4] = False
        self.__lines.append(line)
