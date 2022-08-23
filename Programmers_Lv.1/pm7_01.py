def solution(lottos, win_nums): # solution function defined
    answer = [] # initialize answer
    count = 7 # initialize count
    
    for i in lottos: # repeat until i in lottos
        if i == 0: # if i is 0
            count -= 1 # cont = count - 1
        elif i in win_nums: # else if i in win_nums
            count -= 1 # cont = count - 1
    if count > 6: # if count is bigger than 6
        answer.append(6) # answer append 6
    else :
        answer.append(count) # answer append count
    count = 7 # initialize count
    
    for j in lottos: # repeat until j in lottos
        if j in win_nums: # if j in win_nums
            count -= 1 # cont = count - 1
    if count > 6: # if count is bigger than 6
        answer.append(6) # answer append 6
    else :
        answer.append(count) # answer append count
    
    return answer # return answer