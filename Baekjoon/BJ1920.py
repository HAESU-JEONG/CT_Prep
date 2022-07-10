n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
search_num_list = list(map(int, input().split()))

for i in range(len(search_num_list)):
    if search_num_list[i] in num_list: # if the number you're looking for is on that list
        print(1)
    else:
        print(0)