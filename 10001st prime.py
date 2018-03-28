def is_prime(x):
    if x > 1:
        if x == 2:
            return True
        for i in range(2, int(round((x/2))) + 1):
            if x / i == i:
                return False
            elif x % i == 0:
                return False
        else:
            return True
    else:
        return False

def nextPrime(currentPrime):
    while True:
        currentPrime += 2
        if is_prime(currentPrime):
            return currentPrime

count = 1
currPrime = 1
while count != 10001:
    count += 1
    currPrime = nextPrime(currPrime)
print(currPrime)
