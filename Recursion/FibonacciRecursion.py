def good_fibonacci(n):
    '''Returns a pair of Fibonacci numbers, F(n) and F(n-1)'''
    if n <= 1:
        print(n, 0)
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        print(a + b, a)
        return (a + b, a)

good_fibonacci(5)
