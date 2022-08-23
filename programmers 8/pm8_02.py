def solution(num):
    answer = 0
    first, second = 1, 2

    if num < 2: 
        return 1

    else:
        for i in range(2, num+1):
            first, second = second, first+second

    answer = first % 1234567

    return answer

num = int(input())
print(solution(num))