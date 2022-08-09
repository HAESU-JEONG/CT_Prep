def solution(nums):
    answer = 0
    from itertools import combinations

    for i in combinations(nums, 3):
        com = sum(i)
        for j in range(2, com):
            if com % j == 0 :
                break
        else :
            answer += 1
    return answer 

nums = input()