def solution(price, money, count): # solution function defined
    result = 0 # initialize result
    answer = 0 # initialize answer
    for i in range(count + 1): # repeat until i in range in count + 1
        result = price * i # result is price * i
        answer += result # answer is answer + result
    if money >= answer: # if money is bigger than answer or answer is same answer
        return 0 # return 0
    else: # if money is smaller than answer
        return answer - money # return answer - money
    
price, money, count = map(int, input().split()) # input number
print(solution(price, money, count)) # print solution(price, money, count)