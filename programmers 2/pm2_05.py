def add(num):
    answer = 0
    for i in range(len(str(num))):
        answer += num % 10 
        num = num // 10

    print(answer)

num = int(input())
add(num)