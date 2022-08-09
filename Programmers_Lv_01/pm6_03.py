def solution(absolutes, signs):
    result_list = []
    
    for i in range(len(absolutes)):
        if signs[i] == True: # input data is positive number
            result_list.append(absolutes[i])
        elif signs[i] == False:  # input data is negative number
            result_list.append(absolutes[i] * -1)
    
    return sum(result_list)