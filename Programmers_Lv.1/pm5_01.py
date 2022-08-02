def solution(sizes): # solution function defined
    width = [] # initialize width
    height = [] # initialize height
    answer = 0 # initialize answer
    for i in range(len(sizes)): # repeat until i in range sizes length
        if sizes[i][1] >= sizes[i][0]: # if sizes[i][1] is bigger than sizes[i][0]
            width.append(sizes[i][1]) # append width the biggest one
            height.append(sizes[i][0]) # append height the biggest one
            answer = max(width) * max(height) # answer is the biggest width multiplication the biggest height
        else:
            width.append(sizes[i][0]) # append width the smallest one
            height.append(sizes[i][1]) # append height the smallest one
            answer = max(width) * max(height) # answer is the smallest width multiplication the smallest height
    return answer # return answer