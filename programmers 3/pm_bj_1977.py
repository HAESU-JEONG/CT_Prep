def solution(num1, num2):
    sum= 0
    square_num = []
    for i in range(num1, num2+1):
        if (int(i ** 0.5) ** 2) == i:
            square_num.append(i)
            sum += i

    if square_num :
        print(sum)
        print(square_num[0])

    else : 
         print(-1)

num1, num2 = int(input()), int(input())
solution(num1, num2)