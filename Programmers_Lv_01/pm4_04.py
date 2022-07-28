def solution(price, money, count):
    result = money
    
    for i in range(1, count + 1):
        result = result - (price * i)
    
    if result < 0: # case 1 : money < total price
        result = result * -1
    else: # case 2 : money > total price
        result = 0
    
    return result