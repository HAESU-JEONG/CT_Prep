def solution(s):
    number_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    result = s

    for key, value in number_dic.items():
        result = result.replace(key, value) # change key to value

    return int(result) # change result to an integer form