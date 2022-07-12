def solution(num): # defined function solution(num)
    answer = '' # initialize answer
    if num % 2 == 0: # if num is evennumber
        answer = "Even" # answer is "Even"
    else:
        answer = "Odd" # answer is "Odd"
    return answer # return answer

num = int(input()) # input number
print(solution(num)) # print solution(num)