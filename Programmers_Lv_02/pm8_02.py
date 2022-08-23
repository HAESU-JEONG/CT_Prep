def solution(n):
    if n < 2:
        return n
    
    fib = [1, 2]
    for i in range(2, n):
        fib.append((fib[i-2] + fib[i-1]) % 1234567)
    return fib[-1]