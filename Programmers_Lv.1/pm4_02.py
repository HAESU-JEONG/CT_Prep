def solution(a, b): # solution function defined
    answer = 0 # initialize answer
    if a == b: # if a equals b
        answer = a # answer is a
        return answer # return answer
    elif a > b: # elseif a bigger than b
        for i in range(b, a+1): # repeat i until b to a+1
            answer += i # answer = answer + i
        return answer # return answer
    else:
        for i in range(a, b+1): # repeat i until a to b+1
            answer += i # answer = answer + i
        return answer # return answer
    
a, b = map(int, input().split()) # input number
print(solution(a, b)) # print solution(a, b)