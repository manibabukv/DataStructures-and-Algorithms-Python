import time

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


cache = {}

def fibonacciDP(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = fibonacciDP(n-1) + fibonacci(n-2)
            return cache[n]


def bottomUPFib(n):
    answer = [0,1]
    for i in range(2,n):
        answer.append(answer[i-2]+answer[i-1])
    return answer.pop()


t1 = time.time()
print(fibonacci(40))
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(fibonacciDP(40))
t2 = time.time()
print(t2-t1)
