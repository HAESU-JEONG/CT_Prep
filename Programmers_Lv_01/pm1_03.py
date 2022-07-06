import sys

def harshadNum(numlist, origin_num):
    total = sum(numlist)
    if origin_num % total == 0: # modulo operation
        return True
    else:
        return False

input_num = input()
input_num_save = list(map(int, input_num)) # split number and make list
print(harshadNum(input_num_save, int(input_num))) 