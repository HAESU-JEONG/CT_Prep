t = int(input())

for i in range(t):
    number = input()
    reverse_number = int(str(number)[::-1]) # reverse number
    sum_num = int(number) + int(reverse_number) # sum number and reversed number

    rev_sum_num = int(str(sum_num)[::-1]) # reversed sum number

    if str(sum_num) == str(rev_sum_num): # if sum number is the same reversed sum number
        print("YES")
    else:
        print("NO")