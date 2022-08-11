def solution(numbers): # solution defined function
    answer = 0 # initialize answer variable
    for i in range(10): # repeat until i in range 10
        if i not in numbers: # if i not in numbers
            answer += i # answer = answer + i
    return answer # return answer variable

numbers = map(int, input().split()) # input variable
print(solution(numbers)) # print solution(numbers) # print solution(numbers)