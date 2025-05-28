def russianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        russianDoll(doll - 1) 

# russianDoll(5)
# how recursive is matched in the stack memory
def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    fourthMethod()
    print("I am the third method")

def fourthMethod():
    print("I am the fourth method")
# firstMethod()

def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

# recursiveMethod(4)

def iterableMethod(n):
    while True:
        if n < 1:
            print("n is less than 1")
            return
        else:
            print(n)
            n -= 1

# iterableMethod(4)

def factorial(n):
    assert n >= 0 and int(n) == n, 'number must be positive intger only'
    if n == 0:
        return 1
    else:
        s = n * factorial(n-1)
        return s

# print(factorial(4))

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'number must be an integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))
#RECURSION INTERVIEW QUESTIONS

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'number must be an integer'
    if n == 0:
        return n
    return int(n%10) + sumOfDigits(int(n/10))


def power(base,exp):
    assert exp >= 0 and int(exp) == exp, 'exponent must be an integer'
    if exp == 1: return base
    if exp == 0: return 1
    return base * power(base,exp - 1)

def gcd(m,n):
    assert int(m) == m and int(n) == n, 'number must be an integer'
    if m < 0:
        m = -1 * m
    if n < 0:
        n = -1 * n
    if n == 0:
        return m
    else:
        return gcd(int(n), int(m%n))


def decimalToBinary(n):
    if n == 0:
        return 0
    return n%2 + 10*decimalToBinary(int(n/2))  



