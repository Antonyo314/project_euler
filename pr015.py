def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res



print((factorial(40)/(factorial(20)*factorial(20))))