def solution(s):
    cnt = 0 # save whether the letter's index is odd or even
    result = "" # save changed string
    
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0 # if you meet a blank, reset variable
            result += ' '
            continue
        
        if cnt % 2 == 0 and s[i].islower():
            result += chr(ord(s[i]) - 32) # change lower case to upper case and add letter 
        elif cnt % 2 == 1 and s[i].isupper():
            result += chr(ord(s[i]) + 32) # change upper case to lower case and add letter 
        else:
            result += s[i] # just add letter
        
        cnt = cnt + 1

    return result
