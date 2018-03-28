import time, math
start = time.time()
def d(n):
    total = 1
    if n % 2 == 0:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                if n / i != i:
                    total += i + (n / i)
                else:
                    total += i
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                total += i + (n / i)
    return total

total = 0
for x in range(1, 28124):
    if d(x) <= x:
        total += x
print(total)
elapsed = time.time() - start
print("Time taken: {0} {1}".format(elapsed, "seconds"))
