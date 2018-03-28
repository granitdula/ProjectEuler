##import time
##start = time.time()
##
##def collatz_seq(startVal, List):
##    while startVal > 1:
##        if startVal % 2 == 0:
##            startVal /= 2
##            List.append(int(startVal))
##        else:
##            startVal = 3*startVal + 1
##            List.append(int(startVal))
##    return List
##
##N = 1000000
##maxList = []
##for x in range(3, N + 1, 2): #Multiples of two are probably worth not looping for, because their collatz sequence will end quick due to it being halved often.
##    listOfTerms = [x]
##    listOfTerms = collatz_seq(x, listOfTerms)
##    if len(listOfTerms) > len(maxList):
##        maxList = listOfTerms
##    
##print(maxList[0])
##elapsed = (time.time()-start)
##print("This took: " + str(elapsed) + " seconds.")

#WORK ON EFFICIENCY, because it works but it is too slow. (Takes approx 36s to
#calculate the answer for N = 1000000

#Initial try of the program is above.
#New better version below.
import time

start = time.time()
def next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

lengths = {1:1}  # n -> length of sequence starting from n

def length(n):
    if not n in lengths:
        lengths[n] = 1 + length(next(n))
    return lengths[n]

N = 1000000
Max = 0
for n in range(1,N+1):
    l = length(n)
    if l>Max:
        Max = l
        newN = n
print (newN)

elapsed = (time.time() - start)
print("This took: " + str(elapsed) + " seconds.") 
