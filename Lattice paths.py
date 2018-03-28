import math
import time
start = time.time()

SIDESIZE = 20

def nCr(n, r):
    answer = int((math.factorial(n))/(math.factorial(r)*math.factorial(n-r)))
    return answer
    
def latticePaths(sideLength):
    if sideLength >= 0:
        numOfRoutes = nCr(sideLength*2, sideLength)
        print("There are {0} number of routes.".format(numOfRoutes))
    else:
        print("Error invalid input.")

latticePaths(SIDESIZE)
elapsed = time.time() - start
print("Time taken: {0} seconds".format(elapsed))

#The largest SIDESIZE value is 514 before the answer becomes to big for a float.
