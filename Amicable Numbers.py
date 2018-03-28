import time, math
start = time.time()
# Below is my old less efficient d(n) function
# def d(n):
#     total = 0
#     for i in range(1, int((n/2) + 1)):
#         if n % i == 0:
#             total += i
#     return total

def d(n): ####### This is the improved d(n) function.
    total = 1
    if n % 2 == 0:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                total += i + (n / i)
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                total += i + (n / i)
    return total

l = list(range(1, 10001))
amicableList = []
for num in l:
    if not num in amicableList:
        x = d(num)
        if d(x) == num and num != x:
            amicableList.append(num)
            amicableList.append(x)
print(sum(amicableList))
elapsed = str(time.time() - start)
print("This took: {0} {1}".format(elapsed, 'seconds'))
# Further improvements made shown by hash on the side.
