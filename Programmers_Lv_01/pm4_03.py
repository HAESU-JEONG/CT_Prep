def solution(s):
    length = len(s)
    s_list = list(s)
    result_list = []
    
    if length % 2 == 0:
        result_list.append(s_list[length // 2 - 1]) # append first letter of the two letters in the middle
        result_list.append(s_list[length // 2]) # append second letter of the two letters in the middle
        return ''.join(result_list) 
        
    elif length % 2 == 1:
        result_list.append(s_list[length // 2]) # append the middle letter
        return ''.join(result_list)