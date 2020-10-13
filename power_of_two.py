'Given an integer n, write a function to determine if it is a power of two.'

def isPowerOfTwo(n) :
    while n >= 1:
        if n == 1:
            return True
        n = n / 2    
    return False

print(isPowerOfTwo(2))
print(isPowerOfTwo(3))
print(isPowerOfTwo(16))