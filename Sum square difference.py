total = 0
squaredSum = 0
for x in range(1, 101):
    total += x
    squaredSum += x ** 2
sumSquared = total ** 2
difference = sumSquared - squaredSum
print(difference)
