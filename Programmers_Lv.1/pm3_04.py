def solution(n): # solution function defined
    answer = '' # initialize answer
    for i in range(n): # repeat until i in range n
        if i % 2 == 0: # if i is even number
            answer += "수" # add answer to "수"
        else:
            answer += "박" # add answer to "박"
    return answer # return answer
            
n = int(input()) # input number
print(solution(n)) # print solution(n)