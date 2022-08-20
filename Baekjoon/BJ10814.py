import sys
n = int(sys.stdin.readline().rstrip())

member_list = []

for i in range(n):
    member_age, member_name = map(str, sys.stdin.readline().split())
    member_list.append([int(member_age), member_name])

member_list.sort(key=lambda x:x[0]) # sort by age(member_list[i][0])

for i in range(n):
    print(int(member_list[i][0]), member_list[i][1])