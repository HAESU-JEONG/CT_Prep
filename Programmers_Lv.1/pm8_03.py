def solution(A,B): # solution function defined
    answer = 0 # initialize answer
    A.sort() # sort A
    B.sort() # sort B
    for i in range(len(A)): # repeat until i in range A length
        answer += A[i] * B[len(A) -i - 1] # answer is answer + A[i] * B[len(A) -i - 1]
    return answer # return answer