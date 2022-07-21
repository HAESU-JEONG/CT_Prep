def solution(n):
    result_string = ""
    for i in range(n):
        if i % 2 == 0:
            result_string += "수"
        else:
            result_string += "박"
            
    return result_string