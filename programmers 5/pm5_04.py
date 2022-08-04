def solution(num):
    result = ''
    while num:
        result += str(num % 3)
        num = num // 3
    return int(result, 3)
    

num = int(input())
print(solution(num))