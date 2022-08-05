def solution(n): # solution function defined
    answer = '' # initialize answer
    while(n >= 1): # repeat until n is bigger than 0
        result = n % 3 # result is n / 3 reminder
        n = n // 3 # n is n / 3 share
        answer += str(result) # answer = answer + str(result)
        
    return int(answer, 3) # return int(answer, 3)

n = int(input()) # input number
print(solution(n)) # print solution(n)