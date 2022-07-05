import sys

def solution(phone_number):
    length = len(phone_number)
    phone_number_save = []

    for i in range(length):
        if length - i >= 5: # not the last four numbers
            phone_number_save += '*'
        else: # the last four numbers
            phone_number_save += phone_number[i]

    phone_number_result = ''.join(phone_number_save)

    return phone_number_result

phone_number = sys.stdin.readline()