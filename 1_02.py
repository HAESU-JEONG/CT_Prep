def solution(phone_number):
  new_phone = '' #new phone_number
  for i in range(7): #repeat 7 times
    new_phone += '*' # add * to new_phone 
  new_phone += phone_number[7:] #add last phone_number to new_phone

  return new_phone #return

phone_number = input() 
print(solution(phone_number))
