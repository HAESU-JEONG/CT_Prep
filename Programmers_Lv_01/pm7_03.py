def solution(s):
    result = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            result += 1
        elif s[i] == ')':
            result -= 1
        
        if result < 0: # if result is smaller than 0, ')' is more than '(' => false
            return False
    
    if result == 0: # '(' == ')'
        return True
    else:
        return False