#스택 사용

def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == "(" :
            stack.append(i)

        else :
            if stack == [] :
                answer = False
            
            else : 
                stack.pop()
    
    if stack == [] :
        return answer

    else:
        answer = False
        return answer

s = "(())"
print(solution(s))
