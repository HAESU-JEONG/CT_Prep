def solution(a, b):
    total = 0
    if a == b:
        return a
    else:
        return sum(range(min(a, b), max(a, b) + 1))