prevTerm, curTerm = 1, 2
fibList = []
while curTerm < 4000000:
    if curTerm % 2 == 0:
        fibList.append(curTerm)
    prevTerm, curTerm = curTerm, prevTerm + curTerm
print(sum(fibList))
