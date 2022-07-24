
inform = [] #student's information

for i in range(int(input())):
    name, day, month, year = input().split()
    inform.append([name, int(day), int(month), int(year)])

inform.sort(key=lambda y: (y[3], y[2], y[1] ) #first key is year, second key is month, last key is day
#Default values for sort() are in ascending order

print(inform[-1][0]) #print last student
print(inform[0][0]) #print first student

