import numpy as np
import pygame

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
        #return self.target_func(self.game.get_die_state())
    
    @staticmethod
    def target_func(state):
        #state: key-value list
        #calculate score for state
        dieLoc = state['dieState']# coordinate where bird crashed
        pipeLoc = state['lowerPipe'][0]# coordinate where lower pipe left-up corner

        distance = np.math.sqrt(pow(dieLoc[0]-pipeLoc[0],2)+pow(dieLoc[1]-pipeLoc[1], 2))# distance of crashed to pipe left-up corner
        xDiff = dieLoc[0]-pipeLoc[0]# x coordinate differ

        return distance, xDiff

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

        ### set game parameter ###
        # __state.data    [bird Y , bird speed, pipe X, pipe Y,  isFlap ]
        # @@ Upper left corner is (0,0) @@
        # pipe  width is 52(form spirit/pipe.png), Two pipe gap is 100 (from origin source code).
        birdX = 0
        birdY = self.__state[0]
        birdVelX = 14 #Use pipe shirt in origin game
        birdVelY = self.__state[1]
        birdAccY = 1
        birdFlapAccY = -14
        birdHeight = 24

        pipeLeftX = self.__state[2]
        pipeRightX = pipeLeftX + 52
        upperPipeY = self.__state[3]
        lowerPipeY = upperPipeY + 100
        
        srceenWidth = 288
        screenHeight = 512
        isFlap = self.__state[4]
        die = False
        
        def check_die():
            # Out screen
            if birdX < 0 or birdX > srceenWidth or birdY < 0 or birdY >screenHeight:
                return True
            # hit upper pipe
            elif pipeLeftX <= birdX <= pipeRightX and 0 <= birdY <=upperPipeY:
                return True
            # hit lower pipe
            elif pipeLeftX <= birdX <= pipeRightX and lowerPipeY <= birdY <=screenHeight:
                return True
            else:
                return False
        def print_loc():
            print("X:%d, Y:%d"%(birdX,birdY))
        ### Simulate ###
        # Bird Y accelerate
        if isFlap:
            birdVelY += birdFlapAccY + (-1) #-14
        while not die:
            birdVelY += birdAccY
            # check speed in range
            if birdVelY < -8:
                birdVelY = -8
            elif birdVelY > 10:
                birdVelY = 10
            # Bird Y move
            birdY += min(birdVelY, 404 - birdY - birdHeight)
            # Bird X move
            birdX += birdVelX
            # DB
            print_loc()
            die = check_die()
        print("END")
        print_loc()
        print(self.__state)
