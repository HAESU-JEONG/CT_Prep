def solution(left, right):
    answer = 0
    if left > right : #if left is bigger than right,
        left, right = right, left #change their seat
    
    for i in range(left, right+1): #repeat from left to right + 1
        tmp = 0 #tmp reset 
        for j in range(1, i+1): #repeat from 1 to i+1
            if i % j == 0 : 
                tmp += 1
        
        if tmp % 2 == 0: #if tmp is even number
            answer += i #add 
        else:
            answer -= i 
        
    return answer
    
left, right = map(int, input().split())
print(solution(left, right))