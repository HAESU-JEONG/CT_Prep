def solution(price, money, count):
    total = 0 
    
    for i in range(1, count+1): 
        total += price * i

    return total - money if total - money > 0 else 0 
    #if total - money is bigger than 0, return total - money
    #else return 0

price, money, count= map(int, input().split()) #input 3 variable, split by space, map int 
print(solution(price, money, count)) 