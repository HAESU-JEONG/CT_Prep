def solution(n): # solution defined
    answer = 0 # initialize answer 0
    n = str(n) # Replace numbers with strings
    
    for i in (n): # repeat until n
        answer += int(i) # answer = answer + int(i)
    
    return answer # return answer

n = int(input()) # input number
print(solution(n)) # print solution(n)