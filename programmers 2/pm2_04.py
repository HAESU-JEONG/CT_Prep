def reverse(num):
    re_num = []
    one = 0

    for i in range(len(str(num))):
        one = str(num%10)
        num = num // 10
        re_num.append(one)

    return re_num

num = int(input())
print(reverse(num))