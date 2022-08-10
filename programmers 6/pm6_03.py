def solution(absolutes, signs):
    for i in range(len(absolutes)): #repeat as absolutes's length
        if signs[i] == False: # if signs[i] is False
            absolutes[i] = absolutes[i] * -1 #change absolute[i] to absolutes[i] * -1
    
    return sum(absolutes) #return sum
