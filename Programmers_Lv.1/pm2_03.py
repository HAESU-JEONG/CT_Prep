def solution(n): # defined solution(n)
    answer = -1 # answer is -1
    x = n ** (1 / 2) # One-half square of n is the square root of n.
    if x % 1 == 0: # if x is integer
        return (x + 1) ** 2 # (x + 1) Squeare
    return answer # return answer

n = int(input()) # input number
print(solution(n)) # print solution