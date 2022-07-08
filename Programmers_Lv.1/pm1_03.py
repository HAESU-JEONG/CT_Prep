def solution(x): # solution function defined

    num = str(x) # change string
    add = 0 # initialize add

    for i in range(len(num)): # repeat until num length
        add += int(num[i]) # add = add + int(num[i]) # i increasing by 1

    if (x % add == 0): # if x is divided by add 
        answer = True # answer is true
        return answer # return answer
    else: # else x is not divided by add
        answer = False # answer is false
        return answer # return answer

x = int(input()) # input number
print(solution(x)) # print solution(x)