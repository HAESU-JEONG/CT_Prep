num = int(input())

for i in range(1, num+1):
    print("*"*i + " "*(num-i) + " "*(num-i) + "*"*i)
for i in range(1, num):
    print("*"*(num-i) + " "*i + " "*i +"*"*(num-i))