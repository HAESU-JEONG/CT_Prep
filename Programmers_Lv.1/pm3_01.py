def solution(s): # solution function defined
    answer = '' # initialize answer
    s = s.split(" ") # split by space
    for i in (s): # repeat until s
        for j in range(len(i)): # repeat until length of i
            if j % 2 == 0: # if j is even number
                answer += i[j].upper() # replace uppercase letters
            else:
                answer += i[j].lower() # replace lowercase letters
        answer += ' ' # add spaces
    return answer[:-1] # slice end spaces