def solution(lottos, win_nums):
    answer = []
    same = len(set(lottos) & set(win_nums)) #intersection of lottos and win_nums
    zero = lottos.count(0) # 0 of lottos

    for i in range(1, 7): 
        if (same+zero) == 0: #same+zero = maximum
            answer.append(6)
            break
        
        elif (same+zero) == i :
            answer.append(7-i)

    for i in range(1, 7):    
        if same == 0 : #minimum
            answer.append(6)
            break

        elif same == i :
            answer.append(7-i)
            
    return(answer)

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)
