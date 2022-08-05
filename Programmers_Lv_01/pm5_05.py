def solution(left, right):
    divisor_sum_list = [] # save if the divisor is even
    divisor_sub_list = [] # save if the divisor is odd
    
    for i in range(left, right + 1):
        divisor_cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor_cnt += 1
            
        if divisor_cnt % 2 == 0:
            divisor_sum_list.append(i)
        else:
            divisor_sub_list.append(i)
    
    result = sum(divisor_sum_list) - sum(divisor_sub_list)
    return result