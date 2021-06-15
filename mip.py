
from solve import solve
from solution_represent import solutionRepresent



#solve = solve()

def solveEva(data):
    data.append(True)
    sortData = list(data)
    sortData[1] = data[3]
    sortData[2] = data[1]
    sortData[3] = data[2]
    solution = solutionRepresent(sortData)
    solution.set_better_flaped_choice()
    print(solution.get_solution())
    return solution.get_solution()[4], [(0,0), (0,0)]