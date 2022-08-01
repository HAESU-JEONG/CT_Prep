def solution(sizes):
    width = []
    height = []
    
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0] # swap length
        width.append(sizes[i][0]) # add the longer size to the width list
        height.append(sizes[i][1]) # add the smaller size to the height list

    max_width = max(width)
    max_height = max(height)

    result = max_width * max_height
    
    return result