import math
n = 100
number = math.factorial(n)
total = 0
for char in str(number):
    total += int(char)
print(total)
