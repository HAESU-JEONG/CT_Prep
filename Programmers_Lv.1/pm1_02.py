def solution(phone_number): # solution function defined
    answer = '' #initialize answer
    
    for i in range(len(phone_number)-4): #repeat until phone number length -4
        answer += '*' #answer = answer + '*' #add '*' to the length of phone_number -4
    
    answer += phone_number[-4:] #answer = answer + phone_number[-4:]
    return answer #return answer

phone_number = input() #input phone number
print(solution(phone_number)) #print solution(phone_number)