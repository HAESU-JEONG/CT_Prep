def solution(num):
    answer = ''

    for i in range(1, num+1):
        if (i % 2) == 0: 
            answer += '박'
        else:
            answer += '수'

    return answer

num = int(input())
print(solution(num))