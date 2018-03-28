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
        currentPrime += 1
        if is_prime(currentPrime):
            return currentPrime

number, currPrime = 600851475143, 2
while number > 1:
    if number % currPrime == 0:
        number /= currPrime
    else:
        currPrime = nextPrime(currPrime)
print(currPrime)
