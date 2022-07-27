def solution(str):
    num = int(len(str) / 2)
    if len(str) % 2 == 0 :
        return ''.join(list(str)[num-1:num+1:])

    else:
        return ''.join(list(str)[num:num+1:])

str = input()
print(solution(str))