def solution(numbers):
    result = 0
    for i in range(10):
        if numbers.count(i) == 0:
            result += i
    return result