def solution(a, b):
    save_data = []
    
    for i in range(len(a)):
        save_data.append(a[i]*b[i])
    
    return sum(save_data)