# Recursive Approach
def factorial_recursive(n):
    if n == 2:
        return 2
    
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))

# What actually happening

# 5 * factorial_recursive(4) --> 5 * 4 * factorial_recursive(3) --> 5 * 4 * 3 * factorial_recursive(2) --> 5 * 4 * 3 * 2 = 120 
    


# Iterative Approach
def factorial(n):
    f = 1
    for i in range(n):
        f = f*(i+1)
    return f
        
print(factorial(5))

print(5*4*3*2*1)
        