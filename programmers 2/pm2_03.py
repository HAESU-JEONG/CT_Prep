import math
def sroot(num):
    squre_root = math.sqrt(num)
    if (squre_root % 1) == 0:
        return (squre_root + 1) ** 2

    else :
        return -1

num = int(input())
print(int(sroot(num)))