def fibonacci_number(n):
    assert 0 <= n <= 10**3
    Fibonacci = [0,1]
    for i in range(2,n+1):
        Fibonacci.append(Fibonacci[i-2] + Fibonacci[i-1])
    return Fibonacci[n]
