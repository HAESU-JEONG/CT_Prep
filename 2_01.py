def solution(num):
    answer = 0
    count = 0
    
    while True:
        if num == 1 and 1 < count < 500 :
            return count

        elif num == 1 and count == 1:
            return 0

        elif count > 500:
            return -1

        if (num % 2) == 0:
            num = num / 2
        
        else :
            num = num * 3 + 1
        
        count += 1

num = int(input()) #input number
print(solution(num))