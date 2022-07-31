import heapq
import sys

heap = []

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x == 0 and len(heap) == 0:
        print(0)
        continue
    elif x == 0:
        print(heapq.heappop(heap))
    elif x != 0:
        heapq.heappush(heap, x)