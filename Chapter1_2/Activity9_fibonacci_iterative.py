 ## Activity 10 – the Fibonacci function with an iteration

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
