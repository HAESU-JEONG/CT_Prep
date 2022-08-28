string = list(input())

number = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

min_time = 0

for i in range(len(string)):
    for j in range(len(number)):
        if string[i] in number[j]:
            min_time += j + 2

print(min_time)