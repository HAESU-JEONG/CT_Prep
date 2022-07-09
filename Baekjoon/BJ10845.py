import sys

cnt = int(sys.stdin.readline())
que = [] # FIFO

for i in range(cnt):
    command = []
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        que.insert(0, command[1]) # insert input number at queue[0]

    elif command[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que) - 1]) # print queue's last number
    
    elif command[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0]) # print queue's first number
    
    elif command[0] == 'size':
        print(len(que))

    elif command[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'pop':
        if len(que) != 0:
            print(que.pop()) # delete queue's first number
        else:
            print(-1)
