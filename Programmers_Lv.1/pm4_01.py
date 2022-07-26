def solution(s): # solution function defined
    answer = ''.join(sorted(s)) # s is sorted by in ascending order
    return answer[::-1] # return answer is sorted by in descending order

s = input() # input string
print(solution(s)) # print solution(s)