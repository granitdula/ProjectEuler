import time
start = time.time()

NUMBER = 2
INDEX = 1000

def sumDigits(x):
    answer = sum(map(int, str(x))) #Initial thought.
    return answer

def sumDigits2(x):
    remainder = 0
    while x:
        remainder, x = remainder + (x % 10), x // 10 #Other method from online.
    return remainder

value = NUMBER ** INDEX
answer = sumDigits(value)

elapsed = time.time() - start
print(answer)
print("Time taken: {0} seconds".format(elapsed))
