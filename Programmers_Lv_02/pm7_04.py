def solution(number, k):
    num_stack = [number[0]]
    # initialize to the first number

    for num in number[1:]:
        # num_stack is not blank
        # num_stack's last number is smaller than num
        # k is larger than 0
        while len(num_stack) > 0 and num_stack[-1] < num and k > 0:
            k -= 1 # decrease 'k' by 1
            num_stack.pop() # num_stack's number is pop
        num_stack.append(num) # add new number
    
    # if num_stack's elements are not removed enough
    if k != 0:
        num_stack = num_stack[:-k]
        
    return ''.join(num_stack)