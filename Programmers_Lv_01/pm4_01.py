def solution(s):
    string_list = list(s)
    string_list.sort(reverse=True)
    return ''.join(string_list)