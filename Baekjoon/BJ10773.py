n = int(input())

money_list = []

for i in range(n):
    input_money = int(input())

    if input_money == 0:
        del money_list[len(money_list) - 1]
    
    else:
        money_list.append(input_money)

print(sum(money_list))