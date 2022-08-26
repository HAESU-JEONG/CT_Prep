def solution(n): # solution function defined
    if n < 2: # if n is smaller than 2
        return n # return n
    else:
        return (solution(n - 1) + solution(n - 2)) % 1234567 # return recursive function the rest of 1234567

n = int(input()) # input number
print(solution(n)) # print solution(n)