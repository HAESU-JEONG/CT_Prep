def solution(n):
    arr = list(map(int, str(n))) # separate each number and make list
    rev_arr = list(reversed(arr)) # array reverse
    return rev_arr
