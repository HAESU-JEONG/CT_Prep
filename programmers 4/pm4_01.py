def solution(str):
    return ''.join(sorted(list(str))[::-1])
    #str changes list, and uses sort().
    # [::-1] has reversed list. 
    # make list to ''

str = input()
print(solution(str))