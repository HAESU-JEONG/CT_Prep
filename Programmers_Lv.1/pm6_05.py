def solution(s): # solution function defined
    # alpa defined
    alpa = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'zero' : 0}
    answer = s # answer equals s
    for i in alpa.items(): # repeat until i in alpa // i value is ('one', 1) ('two', 2) ... ('zero', 0)
        answer = answer.replace(i[0], str(i[1])) # alpa replace int
            
    return int(answer) # return int(answer)

s = input() # input string
print(solution(s)) # print solution(s)