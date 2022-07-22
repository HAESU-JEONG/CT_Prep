def solution(s): # solution function defined
    if (len(s) == 4 or len(s) == 6) and s.isdigit(): # if s length is 4 or 6, then and s is integer
        return True # return True if s is an integer number
    else:
        return False # return False if s is not an integer number
            
s = input() # input string value
print(solution(s)) # print solution(s)