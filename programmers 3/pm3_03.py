'''
def solution(str):
    num = int(str) #convert str to int
    return num 

str = input()
print(solution(str))
'''
def solution(str):
    num = int(str) #convert str to int
    return num 

str = input()

while(len(str) >= 5 or len(str) < 1): #Restriction 1. str's length 
    if str[0] != 0 : #Restriction2. the beginning of str isn't 0
        str = input() 

print(solution(str))

