import sys

while True:
    string = sys.stdin.readline().rstrip()

    if string == '.':
        break

    stack = []

    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")

        