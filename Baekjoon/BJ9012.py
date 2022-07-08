TestCase = int(input())
for i in range(TestCase):
    PS = list(input())
    total = 0

    for i in PS:
        if i == "(": 
            total += 1 # if left parentheses are meet, 'total' variable + 1
        elif i == ")":
            total -= 1 # if right parentheses are meet, 'total' variable - 1
        
        if total < 0: # if there are many right parentheses, the pairings of parentheses do not matchc well
            print("NO")
            break
    
    if total > 0:
        print("NO")
    elif total == 0:
        print("YES")
