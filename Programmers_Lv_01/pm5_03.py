from itertools import combinations

def solution(numbers):
    combinations_list = list(combinations(numbers, 2)) # make combinations (you don't have to consider the order)
    sum_combinations_list = []
    
    for i in range(len(combinations_list)):
        sum_combinations_list.append(combinations_list[i][0] + combinations_list[i][1])
    
    sum_combinations_list_set = list(set(sum_combinations_list)) # remove duplicate values
    sum_combinations_list_set.sort() # sorting list
    
    return sum_combinations_list_set