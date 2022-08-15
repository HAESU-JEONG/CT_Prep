
def solution(lottos, win_nums):
    answer = []
    max, min = 0, 0
    zero = 0
    
    for i in range(6):
        if lottos.find(win_nums[i]) != -1:
            min += 1

    for i in range(1, 7):
        if lottos.find(0) != -1:
            max += 1
        max += min

    for i in range(1, 7):
        if min == i :
            answer.append(6-i)
    print(answer)

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)
