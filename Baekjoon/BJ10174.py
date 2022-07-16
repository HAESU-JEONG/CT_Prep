n = int(input())

for i in range(n):
    text = input().lower()
    if list(text) == list(reversed(text)):
        print("Yes")
    else:
        print("No")