import math
for a in range(1, 400):
    for b in range(a+1, 400):
        csquared = a**2 + b**2
        c = math.sqrt(csquared)
        if float(c).is_integer():
            if a + b + c == 1000:
                print(int(a*b*c))
