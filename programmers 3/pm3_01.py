def change(string):
    ch_s = ''

    for i in range(len(string)):
        if i % 2 == 0 :
            ch_s += string[i].upper()
        else :
            ch_s += string[i].lower()
    return ch_s

string = input()
print(change(string))