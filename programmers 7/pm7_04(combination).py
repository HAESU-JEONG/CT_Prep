from itertools import combinations
def solution(number, k) : 
    answer = ''
    output_numbers = []

    output_numbers = list(combinations(number, len(number)-k))
    answer = list(max(output_numbers))
    answer = ''.join(answer)

    return answer


number = "4177252841"
k = 2
print(solution(number, k))