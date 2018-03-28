import time

start = time.time()

SINGLEDIGITNUM = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
DOUBLEDIGITNUM = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
HUNDRED = 7
THOUSAND = 8

total = 0
for i in range(1, 1000):
    c = int(i % 10) # singles digit
    b = int(((i % 100) - c) / 10) # tens digit
    a = int(((i % 1000) - (b * 10) - c) / 100) # hundreds digit
    
    if a != 0:
        total += SINGLEDIGITNUM[a] + HUNDRED
        if b != 0 or c != 0: total += 3 # From the word "and".
    if b == 0 or b == 1:
        total += SINGLEDIGITNUM[(b*10) + c]
    else:
        total += DOUBLEDIGITNUM[b] + SINGLEDIGITNUM[c]
total += SINGLEDIGITNUM[1] + THOUSAND
print(total)

elapsed = time.time() - start
print("Time taken: {0} seconds".format(elapsed))
