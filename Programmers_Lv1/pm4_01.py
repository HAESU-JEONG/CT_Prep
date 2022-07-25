def solution(s):
    # Place strings in descending order and return them as strings again
    answer = "".join(sorted(s, reverse=True))
    return answer
