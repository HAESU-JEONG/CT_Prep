def solution(number, k): # solution function defined
    answer = [] # initializae answer stack
    for i in number: # repeat until i in number
        while answer and answer[-1] < i and k > 0: # repeat until answer and answer[-1] is smaller than i and k is bigger than 0
            answer.pop() # delete value and obtain deleted value
            k -= 1 # k = k - 1
        answer.append(i) # append answer i
    if k > 0: # if k is bigger than 0
        answer = answer[:-k] # delete value has not been deleted
    
    return ''.join(answer) # return answer