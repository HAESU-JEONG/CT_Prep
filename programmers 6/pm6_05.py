def solution(ori):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    number_s = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(number)):
        if ori.find(number_s[i]) != -1:
            ori = ori.replace(number_s[i], number[i])
    return int(ori)

ori = input()
print(solution(ori)) 