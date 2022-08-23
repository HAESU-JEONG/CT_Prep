def solution(n):
    answer = 0
    first, second  = 0, 1

    for i in range(2, n+1):
        first, second = second, first+second

    answer = second % 1234567
        
    return answer

n = int(input())
print(solution(n))