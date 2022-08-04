def solution(n):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        # divmod function explanation
        # divide an input data by 3
        # and find the quotient and remainder at the same time

        rev_base += str(mod)
        # save remainder at rev_base
    
    return int(rev_base, 3)
    # change reversed ternary number to decimal number