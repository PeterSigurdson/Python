def factorial(n):
    if n == 1:
        print('point A: n is ', n)
        return 1
    else:
        print('point B: n is ', n)
        return n * factorial(n-1)

print(factorial(5)  
