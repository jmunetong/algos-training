def fibonacci(n):
    if n <= 2:
        return 1
    fib = [0] * n
    fib[0] =1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n-1]

if __name__ == '__main__':
    print(fibonacci(20))
