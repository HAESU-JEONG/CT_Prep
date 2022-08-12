from itertools import combinations # use combinations

def solution(nums): # defined solution function
    answer = 0 # initialization answer
    three_list = list(combinations(nums, 3)) # combinations of three
    for i1, i2, i3 in three_list: # repeat until i1, i2, i3 in three_list
        if isprime(i1 + i2 + i3): # if i1 + i2 + i3 is prime
            answer += 1 # answer is answer + 1
    return answer # return answer

def isprime(add): # defined prime function
    for i in range(2, add): # repeat until i in range(2, add)
        if add % i == 0: # if add % i is not prime
            return False # return False
    return True # return True

nums = map(int, input().split()) # input list number
print(solution(nums)) # print solution(nums)