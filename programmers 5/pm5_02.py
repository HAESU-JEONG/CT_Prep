def solution(month, day):
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # date of month
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'] # weekend

    tmp = sum(date[:month-1]) + day # add date before month and add date
    return week[(tmp % 7)-1]

month, day = map(int, input().split())
print(solution(month, day))