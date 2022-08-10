def solution(absolutes, signs): # solution function defined
    answer = 0 # initialize answer
    for i in range(len(signs)): # repeat until i in range signs length
        if signs[i]: # if sings[i] is positive number
            answer += absolutes[i] # answer = answer + absolutes[i]
        else: # if signs[i] is negative number
            answer -= absolutes[i] # answer = answer - absolutes[i]
    return answer # return answer