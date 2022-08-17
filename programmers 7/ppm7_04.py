def solution(number, k):
    stack = []

    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
        k -= 1
    

    
    return ''.join(stack)
        

            



    




number = "4177252841"
k = 2
print(solution(number, k))