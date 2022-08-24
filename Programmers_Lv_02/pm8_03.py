def solution(A,B):
    result = 0
    length = len(A)
    A.sort()
    B.sort()
    
    for i in range(length):
        result += A[i] * B[length - 1 - i]
        
    return result