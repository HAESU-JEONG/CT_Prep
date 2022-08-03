def solution(a, b): # solution function defined
    answer = 0 # initialize answer
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # month number
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'] # day string

    if a > 12 and b > 31: # if a is bigger than 12 and b is bigger than 31
        return 0 # return 0

    for i in range(a - 1): # repeat until i in range a - 1
        answer += month[i] # answer = answer + month[i]

    answer += b - 1 # answer = answer + (b - 1)
    answer = answer % 7 # answer divided by 7's remainder
    answer = day[answer] 
    return answer # return answer

a, b = map(int, input().split()) # input number
print(solution(a, b)) # print solution(a, b)