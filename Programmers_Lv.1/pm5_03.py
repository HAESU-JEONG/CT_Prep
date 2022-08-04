def solution(numbers): # solution defined function
    answer = [] # initialize answer list
    for i in range(len(numbers)): # repeat until i in range numbers length
        for j in range(i + 1, len(numbers)): # repeat until j in range i + 1 to numbers length
            if numbers[i] + numbers[j] not in answer: # if numbers[i] + numbers[j] not in answer
                answer.append(numbers[i] + numbers[j]) # add numbers[i] + numbers[j] to answer
    answer.sort() # sort answer list
    return answer # return answer list

numbers = list(map(int, input().split())) # input list
print(solution(numbers)) # print solution(numbers)