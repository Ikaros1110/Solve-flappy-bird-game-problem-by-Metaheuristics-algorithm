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
        dieLoc = state['dieState']# coordinate where bird crashed
        pipeLoc = state['lowerPipe'][0]# coordinate where lower pipe left-up corner

        distance = np.math.sqrt(pow(dieLoc[0]-pipeLoc[0],2)+pow(dieLoc[1]-pipeLoc[1], 2))# distance of crashed to pipe left-up corner
        xDiff = dieLoc[0]-pipeLoc[0]# x coordinate differ

        return distance, xDiff

class miniGame:
    def __init__(self):
        self.__state = []# State need to train
        self.__dieState = []# Die State, key-value list

        #instant
        self.SCREENWIDTH = 288
        self.PLAYERX = self.SCREENWIDTH * 0.2

    def set_state(self, data):
        #set game state
        self.__state = data
    
    def get_die_state(self):
        #get game state
        return self.__dieState

    def play(self):
        #simulate game playing
        return
    