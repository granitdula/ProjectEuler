import time

start = time.time()

def NextTriNum(currentTriNum, nextTermNumber):
    NewTriNum = currentTriNum + nextTermNumber
    return NewTriNum

def CountFactors(x):
    count = 2
    for i in range(2, int(round(x**0.5)) + 1): # Write on paper and see how the program runs, notice inefficient patterns and solve for new algorithm.
        if x % i == 0:
            count += 2
        if i * i == x:
            count -= 1
    return count

termNum = 1
currNum = 1
numberOfFactors = 0
while numberOfFactors <= 500:
    termNum += 1
    currNum = NextTriNum(currNum, termNum)
    numberOfFactors = CountFactors(currNum)
print(currNum)

elapsed = (time.time() - start)
print("This algorithm took: " + str(elapsed) + " seconds.")
