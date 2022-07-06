def harshad(num):
    add_num = 0
    new_num = num 

    while(num > 0):
      add_num += (num%10)
      num = num//10

    if ((new_num % add_num) == 0 ):
      answer = True
      return answer

    else:
      answer = False
      return answer

num = int(input())
print(harshad(num))
