from itertools import combinations

def solution(nums):
    combinations_num_list = list(combinations(nums, 3)) # make combinations list
    combinations_num_sum_list = []
    cnt = 0

    for i in range(len(combinations_num_list)):
        combinations_num_sum_list.append(combinations_num_list[i][0] + combinations_num_list[i][1] + combinations_num_list[i][2]) # sum combinations elements 
    
    for i in combinations_num_sum_list:
        check = True # check whether number is prime number
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        
        if check == True: # if number is prime, check's value is true.
            cnt += 1
    
    return cnt