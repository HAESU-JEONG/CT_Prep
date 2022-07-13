def solution(n):
    x = n**(1/2) # x is the square root n
    if int(x) == x: # if x is integer type
        return (x+1)*(x+1)
    else: # x isn't integer type
        return -1