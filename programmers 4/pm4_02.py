def solution(num1, num2):
    sum = 0
    if num1 > num2 : #if num1 is larger than num2
        num1, num2 = num2, num1 # change their seats

    elif num1 == num2 : #if num1 equals num2 
        return num1 #return num1 

    for i in range(num1, num2+1): #repeat num1 to num2+1
        sum += i # add 
    return sum 



num1, num2 = input().split() #input two things and split by space
num1 = int(num1) #change int
num2 = int(num2) 
print(solution(num1, num2))