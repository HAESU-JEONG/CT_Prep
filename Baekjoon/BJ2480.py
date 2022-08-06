num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3: # case1 : all numbers are same
    print(10000+num1*1000)
elif num1 == num2 or num2 == num3: # case2 : num1 or num3 is the same as num2
    print(1000+num2*100)
elif num1 == num3: # case3 : num1 is the same as num3
    print(1000+num1*100)
else: # all numbers are different
    print(max(num1, num2, num3) * 100)