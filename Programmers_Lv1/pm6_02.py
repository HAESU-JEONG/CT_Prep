def solution(a, b):
    # Initialize variable
    answer = 0
    # for 0 to a length
    for i in range(0, len(a)):
        answer += a[i] * b[i]
    return answer
