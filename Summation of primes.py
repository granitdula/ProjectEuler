def is_prime(x):
    if x > 1:
        if x == 2:
            return True
        for i in range(3, int(round((x**0.5))) + 1):
            if x / i == i:
                return False
            elif x % i == 0:
                return False
        else:
            return True
    else:
        return False

def nextPrime(currentPrime):         #This is my solution, however it isn't the
    while True:                      #most efficient, search the sieve of 
        currentPrime += 2            #eratosthenes.
        if is_prime(currentPrime):
            return currentPrime

Sum = 2
currPrime = 3

while currPrime <= 2000000:
    Sum += currPrime
    currPrime = nextPrime(currPrime)

print(Sum)
