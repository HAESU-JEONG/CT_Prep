import sys

def solution(phone_number):
    length = len(phone_number)
    phone_number_save = []

    for i in range(length):
        if length - i >= 5:
            phone_number_save += '*'
        else:
            phone_number_save += phone_number[i]

    phone_number_result = ''.join(phone_number_save)

    return phone_number_result

phone_number = sys.stdin.readline()