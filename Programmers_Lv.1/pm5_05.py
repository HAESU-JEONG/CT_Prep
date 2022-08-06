def solution(left, right): # solution function defined
    answer = 0 # initialize answer
    for i in range(left, right + 1): # repeat until i in range left to right + 1
        cnt = 0 # initialize cnt
        for j in range(1, i + 1): # repeat until j in range 1 to i + 1
            if i % j == 0: # if i divided by j is 0
                cnt += 1 # then cnt = cnt + 1
        if cnt % 2 == 0: # if cnt divided by 2 is 0
            answer += i # answer = answer + i
        else:
            answer -= i # answer = answer - i
    return answer # return answer

left, right = map(int, input().split()) # input number
print(solution(left, right)) # print solution(left, right)