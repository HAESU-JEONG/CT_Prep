def solution(number, k):
    stack = [number[0]] #input firtst number to stack 

    for num in number[1:]: #start numner[1], repeat
        while stack and stack[-1] < num and k > 0:  #previous number is smaller than next num and k is bigger than 0
            k -= 1 # take one out of k
            stack.pop() #pop() 
        stack.append(num) #append()

    if k != 0: #if k isn't 0
        stack = stack[:-k]  #stack

    return ''.join(stack) 