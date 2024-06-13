def nFacRuntimeFunc(n):
    for i in range(n):
        nFacRuntimeFunc(n-1)

# The function calls itself n times for the input n.
# Each recursive call decrements the input value by 1 until it reaches 0.
# So, the total number of recursive calls is n * (n-1) * (n-2) * ... * 1, which is equivalent to n! (n factorial).