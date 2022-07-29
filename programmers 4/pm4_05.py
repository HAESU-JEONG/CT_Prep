def solution(num):
    for i in range(2, num):
        if num % i == 1 :
            return i 

num = int(input())
print(solution(num))