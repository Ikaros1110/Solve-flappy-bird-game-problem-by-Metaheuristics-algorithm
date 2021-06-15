import cvxpy as cvx
import numpy as np
import matplotlib.pyplot as plt
from solve import solve
from solution_represent import solutionRepresent


N = 24 # time steps to look ahead
path = cvx.Variable((N, 2)) # initialize the y pos and y velocity
flap = cvx.Variable(N-1, boolean=True) # initialize the inputs, whether or not the bird should flap in each step
last_solution = [False, False, False] # seed last solution
last_path = [(0,0),(0,0)] # seed last path

PIPEGAPSIZE  = 100 # gap between upper and lower pipe
PIPEWIDTH = 52
BIRDWIDTH = 34
BIRDHEIGHT = 24
BIRDDIAMETER = np.sqrt(BIRDHEIGHT**2 + BIRDWIDTH**2) # the bird rotates in the game, so we use it's maximum extent
SKY = 0 # location of sky
GROUND = (512*0.79)-1 # location of ground
PLAYERX = 57 # location of bird


def getPipeConstraintsDistance(x, y, lowerPipes):
    constraints = [] # init pipe constraint list
    pipe_dist = 0 # init dist from pipe center
    for pipe in lowerPipes:
        dist_from_front = pipe['x'] - x - BIRDDIAMETER
        dist_from_back = pipe['x'] - x + PIPEWIDTH
        if (dist_from_front < 0) and (dist_from_back > 0):
            constraints += [y <= (pipe['y'] - BIRDDIAMETER)] # y above lower pipe
            constraints += [y >= (pipe['y'] - PIPEGAPSIZE)] # y below upper pipe
            pipe_dist += cvx.abs(pipe['y'] - (PIPEGAPSIZE//2) - (BIRDDIAMETER//2) - y) # add distance from center
    return constraints, pipe_dist
solve = solve()
def solveEva(data):
    data.append(True)
    solution = solutionRepresent(data)
    solution.set_better_flaped_choice()
    return solution.get_solution()[4], [(0,0), (0,0)]