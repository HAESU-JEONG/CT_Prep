def solution(n):
    divisor_sum = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum