def solution(s): # solution function defined
    answer = '' # initialize answer
    mid = len(s) # change string value
    if mid % 2 == 0: # if mid is even number
        answer = s[mid // 2 - 1] + s[mid // 2] # 
    else:
        answer = s[mid // 2]
    return answer # return answer

s = input() # input string
print(solution(s)) # print solution(s)