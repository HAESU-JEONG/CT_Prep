import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

m = int(input())
search_num_list = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = len(num_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if num_list[mid] == target:
            return True
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

for i in range(m):
    if binary_search(search_num_list[i]):
        print(1)
    else:
        print(0)