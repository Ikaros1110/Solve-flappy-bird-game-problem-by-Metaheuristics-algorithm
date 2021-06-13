import numpy as np


class evaluation:
    def __init__(self):
        self.data = []
        self.game = miniGame()

    def __call__(self ,data):
        #set state for mini game
        self.data = data
        self.game.set_state(self.data)

        #play
        self.game.play()
        
        #calculate answer
        return self.target_func(self.game.get_die_state())
    
    @staticmethod
    def target_func(state):
        #state: key-value list
        #calculate score for state
        dieLoc = state['dieLoc'] # coordinate where bird crashed
        #  standard structure: { 'upperPipeLoc':[[pipeLeftX, upperPipeY], [pipeRightX, upperPipeY]] }
        pipeLeftX = state['upperPipeLoc'][0][0]
        pipeRightX = state['upperPipeLoc'][1][0]
        upperPipeY = state['upperPipeLoc'][0][1]
        lowerPipeY = state['lowerPipeLoc'][0][1]
        screenWidth = 288
        screenHeight = 512
        ### Complete Partition ###
        existPoint = 0 # store front state point
        # 1.die in upperPipe bottom
        if  pipeLeftX <= dieLoc[0] < pipeRightX and upperPipeY-1 <= dieLoc[1] <= upperPipeY+1:
            return existPoint + dieLoc[0]
        existPoint += pipeRightX # max dixLoc[0]

        # 2.die in upperPipe left side
        if pipeLeftX-1 <= dieLoc[0] <= pipeLeftX+1 and dieLoc[1] <= upperPipeY:
            return 300 + existPoint + dieLoc[1] # +300 to ensure dieLoc[1] is minus can run correct(not overlapping).
        existPoint += (300+upperPipeY) # max dieLoc[1]

        # 3.die in ground before pipe
        if dieLoc[0] <= pipeLeftX and screenHeight-1 <= dieLoc[1] <= screenHeight+1:
            return existPoint + dieLoc[0]
        existPoint += pipeLeftX # max dieLoc[0]

        # 4.die in lowerPipe left side
        if pipeLeftX-1 <= dieLoc[0] <= pipeLeftX+1 and lowerPipeY <= dieLoc[1] <= screenHeight:
            return existPoint + screenHeight - dieLoc[1] # direct in contrast
        existPoint += screenHeight  # max point

        # 5.die in lowerPipe top
        if  pipeLeftX <= dieLoc[0] <= pipeRightX and lowerPipeY-1 <= dieLoc[1] <= lowerPipeY+1:
            return existPoint + dieLoc[0]
        existPoint += pipeRightX # max dieLoc[0]

        # 6.die in ground after pipe
        if pipeRightX <= dieLoc[0] <= screenWidth and screenHeight-1 <= dieLoc[1] <= screenHeight+1:
            return existPoint + dieLoc[1]
        existPoint += screenWidth # max dieLoc[0]

        # 7.die in right screen
        if screenWidth-1 <= dieLoc[0] <= screenWidth+1:
            return existPoint + (screenHeight - dieLoc[1]) # direct in contrast
        # existPoint += screenHeight  # max point

        # 8.other
        return 0

        # distance = np.math.sqrt(pow(dieLoc[0]-pipeLoc[0],2)+pow(dieLoc[1]-pipeLoc[1], 2))# distance of crashed to pipe left-up corner
        # xDiff = dieLoc[0]-pipeLoc[0]# x coordinate differ

        # return distance, xDiff



class miniGame:
    def __init__(self):
        self.__state = []# State need to train
        self.__dieState = []# Die State, key-value list

    def set_state(self, data):
        #set game state
        self.__state = data
    
    def get_die_state(self):
        #get game state
        return self.__dieState

    def play(self):
        #simulate game playing

        # __state.data    [bird Y , bird speed, pipe X, pipe Y,  isFlap ]
        # @@ Upper left corner is (0,0) @@
        # pipe  width is 52(form spirit/pipe.png), two pipe gap is 100 (from origin source code).

        ### set game parameter ###
        birdX = 0 + 34 # bird width
        birdY = self.__state[0] + 12 # bird half weight
        birdVelX = 14 # use pipe shirt in origin game
        birdVelY = self.__state[1]
        birdAccY = 1
        birdFlapAccY = -14
        birdHeight = 24

        pipeLeftX = self.__state[2]
        pipeRightX = pipeLeftX + 52
        upperPipeY = self.__state[3]
        lowerPipeY = upperPipeY + 100
        
        screenWidth = 288
        screenHeight = 512
        isFlap = self.__state[4]
        
        ### check bird is dead? ###
        def check_die():
            # Out screen , beside up (To use target_function)
            if birdX <= 0 or birdX >= screenWidth or birdY >=screenHeight:
                return True
            # hit upper pipe and extend up
            elif pipeLeftX <= birdX <= pipeRightX and birdY <= upperPipeY:
                return True
            # hit lower pipe
            elif pipeLeftX <= birdX <= pipeRightX and lowerPipeY <= birdY <= screenHeight:
                return True
            else:
                return False

        ### Simulate ###
        # Bird Y accelerate
        if isFlap:
            birdVelY += birdFlapAccY + (-1) #-14 ,-1 is resist drop (by birdVelY += birdAccY # +1)
        die = check_die()
        while not die:
            # Bird Y drop
            birdVelY += birdAccY # +1
            # check speed in range
            if birdVelY < -8:
                birdVelY = -8
            elif birdVelY > 10:
                birdVelY = 10
            precision = 100 # To strengthen motion trajectory
            for _ in range(precision):
                # Bird Y move
                birdY += min(birdVelY, 404 - birdY - birdHeight)/precision # min() from source code
                # Bird X move
                birdX += birdVelX/precision
                # update die
                die = check_die()
                # debug message
                # print(birdX, birdY)
                if die:
                    break
        # store die state
        self.__dieState = {'dieLoc':[birdX, birdY],
                           'upperPipeLoc':[[pipeLeftX, upperPipeY], [pipeRightX, upperPipeY]],
                           'lowerPipeLoc':[[pipeLeftX, lowerPipeY], [pipeRightX, lowerPipeY]],
                           'screenSize':[screenWidth, screenHeight]}