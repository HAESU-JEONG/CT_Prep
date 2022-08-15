def solution(lottos, win_nums):
    zero_cnt = lottos.count(0) # count zero
    rank = [6, 6, 5, 4, 3, 2, 1] # zero right, one right, two right, three right, four right, five right, six right
    cnt = 0 

    for i in range(len(lottos)): 
        if lottos[i] in win_nums:
            cnt += 1
    
    return rank[zero_cnt + cnt], rank[cnt]