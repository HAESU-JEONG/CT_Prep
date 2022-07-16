def solution(x,n):
    num_list = []

    for i in range(n):
        num_list.append(x*(i+1))

    return(num_list)
   
start = int(input())
num = int(input())

print(solution(start, num))