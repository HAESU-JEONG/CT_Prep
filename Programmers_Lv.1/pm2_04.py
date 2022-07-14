def solution(n): # solution function defined
    n = str(n) # string representation
    answer = [] # answer initialize list
    
    for i in (n): #repeat until n
        answer.append(int(i)) # append i in answer
    answer = answer[::-1] # reverse answer
    return answer # return answer

n = int(input()) # input number
print(solution(n)) # print solution(n)