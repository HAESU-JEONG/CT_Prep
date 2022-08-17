def solution(number, k):
    stack = []

    for i in number:
        if k > 0 :
            while stack and stack[-1] < i :
                stack.pop()
                k+=1

        else : 
            break
        
        stack.append(i)
        k-=1
        
    return ''.join(stack)
        
number = "4321"
k = "1"
            



    




number = "4177252841"
k = 2
print(solution(number, k))