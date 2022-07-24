from collections import deque
import sys

n = int(input())
queue = deque()

for i in range(n):
    input_list = sys.stdin.readline().split()

    if input_list[0] == "push_front":
        queue.appendleft(input_list[1])
    
    elif input_list[0] == "push_back":
        queue.append(input_list[1])
    
    elif input_list[0] == "pop_front":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    
    elif input_list[0] == "pop_back":
        if not queue:
            print(-1)
        else:
            print(queue.pop())

    elif input_list[0] == "size":
        print(len(queue))
    
    elif input_list[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    
    elif input_list[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif input_list[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[len(queue) - 1])
    
