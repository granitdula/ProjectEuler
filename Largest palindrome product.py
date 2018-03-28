def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

loop = True
while loop:
    largestPalindrome = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b
            if is_palindrome(product) and product > largestPalindrome:
                largestPalindrome = product
    loop = False
print(largestPalindrome)
