def solution(num): # solution function defined
    answer = 0 # initialize answer
    
    if num == 1: # if num is 1
        return 0 # return 0
    
    for i in range(500): # repeat until i in range 500
        if num % 2 == 0: # if num is even number
            num = num / 2
            answer += 1 # answer = answer + 1
            if num == 1: # if num is 1
                return answer # return answer
        
        else:
            num = (num * 3) + 1
            answer += 1 # answer = answer + 1
            if num == 1: # if num is 1
                return answer # return answer
        
    return -1 # return -1

num = int(input()) # input number
print(solution(num)) #print solution(num)