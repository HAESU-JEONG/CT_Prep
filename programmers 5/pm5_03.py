def solution(numbers):
    sum = []
    for i in range(len(numbers)): #repeat as much as 'numbers'
        for j in range(i+1, len(numbers)): #repeat from i+1 to numbers
            tmp = numbers[i]+ numbers[j] #sum 
            sum.append(tmp) #append
    return sorted(set(sum)) #set and sorted 

numbers = list(map(int, input().split()))
print(solution(numbers))