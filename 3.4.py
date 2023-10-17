import json

# Создание и заполнение текстового файла
with open("firm_data.txt", "w") as file:
    file.write("firm_1 ООО 10000 5000\n")
    file.write("firm_2 ЗАО 8000 4000\n")
    file.write("firm_3 АО 12000 15000\n")
    file.write("firm_4 ООО 5000 7000\n")

# Чтение файла и вычисление прибыли каждой компании
profits = []
with open("firm_data.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        name = data[0]
        revenue = int(data[2])
        costs = int(data[3])
        profit = revenue - costs
        profits.append(profit)

# Вычисление средней прибыли
average_profit = sum(profit for profit in profits if profit > 0) / len(profits)

# Создание списка с фирмами и их прибылями, а также средней прибылью
firm_list = [{f"firm_{i+1}": profit} for i, profit in enumerate(profits)]
firm_list.append({"average_profit": average_profit})

# Сохранение списка в виде json-объекта
with open("firm_list.json", "w") as file:
    json.dump(firm_list, file)

