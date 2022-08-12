def solution(ori):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    number_s = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(number)):
        if ori.find('number_s[i]'):
            ori.strip('number_s[i]')
            
    return ori

ori = input()
print(solution(ori))