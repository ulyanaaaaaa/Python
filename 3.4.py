import json

with open("firm_data.txt", "w") as file:
    file.write("firm_1 ООО 10000 5000\n")
    file.write("firm_2 ЗАО 8000 4000\n")
    file.write("firm_3 АО 12000 15000\n")
    file.write("firm_4 ООО 5000 7000\n")

profits = []
with open("firm_data.txt", "r") as file:
    for line in file:
        data = line.split() #разделение на списки по пробелам
        name = data[0]
        revenue = int(data[2])
        costs = int(data[3])
        profit = revenue - costs
        profits.append(profit) #добавление в список

len = 0
for profit in profits:
    if profit > 0:
        len=len+1

average_profit = sum(profit for profit in profits if profit > 0) / len #сумма всех положительных значений

firm_list = [{f"firm_{i+1}": profit} for i, profit in enumerate(profits)] #список из словарей
firm_list.append({"average_profit": average_profit})  #добавление словаря

with open("firm_list.json", "w") as file:
    json.dump(firm_list, file)

print(json.dumps(firm_list))

