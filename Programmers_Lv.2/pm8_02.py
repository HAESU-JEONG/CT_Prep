def solution(n): # solution function defined
    n1 = 1 # initialize n1 1
    n2 = 2 # initialize n2 2
    
    for i in range(1, n): # repeat until i in range 1 ~ n
        n1, n2 = n2, n1 + n2 # n1 = n2, n2 = n1 + n2
        
    return n1 % 1234567 # return n1 % 1234567

n = int(input()) # input number
print(solution(n)) # print solution(n)