def solution(num1, num2):
    answer = 0
    for i in range(len(num1)):
        answer += num1[i] * num2[i]
    return answer