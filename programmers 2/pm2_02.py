def distinguish(num):
    if (num % 2) == 0:
        return "Even"

    else:
        return "Odd"

num = int(input())
print(distinguish(num))