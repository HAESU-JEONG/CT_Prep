import sys

n = int(sys.stdin.readline().rstrip())

curr, next = 0, 1
for _ in range(n):
    curr, next = next, curr + next

print(curr)