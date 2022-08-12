def solution(a, b): # defined solution function
    answer = 0 # initialize answer
    for i in range(len(a)): # repeat until i in range a length
        answer += a[i] * b[i] # answer = answer + a[i] * b[i]
    return answer # return answer