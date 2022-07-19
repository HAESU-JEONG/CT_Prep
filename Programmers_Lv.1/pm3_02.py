from re import S


def solution(n): # defined solution function
    answer = 0 # initialize answer 0
    for i in range(1, n + 1): # repeat until i in range 1, n + 1
        if (n % i == 0): # if i is the measure(mineral number) of n
            answer += i # answer = answer + i
    return answer # return answer

n = int(input()) # input number
print(solution(n)) # print solution(n)