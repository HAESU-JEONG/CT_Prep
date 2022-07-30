def solution(n): # solution function defined
    answer = 0 # initialize answer
    for i in range(1, n): # repeat until i in range 1 to n
        if n % i == 1: # if n % i is 1
            answer = i # answer is i
            return answer # return answer

n = int(input()) # input number
print(solution(n)) # print solution(n)