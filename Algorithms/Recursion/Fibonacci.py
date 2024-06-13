# Using Iterative Approach

def fibonacciIterative(n):
    fib1 = 0
    fib2 = 1
    if n < 2:
        return n
    for i in range(n-1):
        fib_i = fib1 + fib2
        fib1 = fib2
        fib2 = fib_i
    return fib_i

print(fibonacciIterative(2))

# Uisng Recursive Approach

def fibonacciRecursive(n):
    if n < 2:
        return n

    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print(fibonacciRecursive(8))
