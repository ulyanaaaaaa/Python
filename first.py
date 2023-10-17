# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
# 1
def number_1(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

count = 0
i = 2
while count != 1001:
    if number_1(i):
        print(i)
        count += 1
    i += 1
# 2
def number_2():
    str = input("Enter str: ")
    for i in str:
        if i.isnumeric():
            print(i)

#3
def number_3():
    f = 0
    flag = 0
    spis = list(input("Enter number spisok: "))
    for i in spis:
        if i.isnumeric():
            f = 0
        else:
            f = 1

    if(f == 0):
        spis.sort()
        for i in spis:
            if int(i) % 2 != 0 and flag == 0:
                print(i)
                flag = 1
    else:
        print("Введена некорректная сторока")
        return number_3()


def number_35():
    list = []
    for i in range(0, 30):
        num = random.randint(-3000, 3000)
        list.append(num)
    print(list)
    min_abs = abs(list[0])
    for num in list:
        if abs(num) < min_abs:
            min_abs = abs(num)
    print(min_abs)
# 4
def number_4():
    str1 = "Enjoy every moment"
    my_dict = dict()
    for letter in str1:
        if letter not in my_dict:
            my_dict[letter] = str1.count(letter)
    print(my_dict)

# 5
def number_5():
    bouquets = {
        "Розы": ["Розы", 500, 10],
        "Гвоздики": ["Гвоздики", 300, 15],
        "Лилии": ["Лилии", 400, 8],
        "Тюльпаны": ["Тюльпаны", 200, 20]
    }


    def show_description():
        for bouquet, info in bouquets.items():
            print(f"{bouquet}: {info[0]}")


    def show_price():
        for bouquet, info in bouquets.items():
            print(f"{bouquet}: {info[1]}")


    def show_quantity():
        for bouquet, info in bouquets.items():
            print(f"{bouquet}: {info[2]}")


    def show_all_info():
        for bouquet, info in bouquets.items():
            print(f"{bouquet}: {info[0]}, Цена: {info[1]}, Количество: {info[2]}")


    def purchase():
        total_price = 0
        while True:
            bouquet = input("Введите название букета (или 'n' для выхода): ")
            if bouquet == 'n':
                break

            if bouquet in bouquets:
                quantity = input("Введите количество: ")
                if quantity.isnumeric():
                    quantity = int(quantity)
                    if quantity <= bouquets[bouquet][2]:
                        bouquets[bouquet][2] -= quantity
                        total_price += bouquets[bouquet][1] * quantity
                    elif quantity < 0:
                        print("Введите корректное количество")
                        return purchase()
                    else:
                        print("Недостаточно товара в магазине.")
                else:
                    print("Введите корректное значение")
            else:
                print("Такого букета нет в магазине.")



        print(f"Общая стоимость покупки: {total_price}")
        print("Остаток товара в магазине:")
        show_quantity()


    def goodbye():
        print("До свидания!")


# Главное меню
    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            show_description()
        elif choice == '2':
            show_price()
        elif choice == '3':
            show_quantity()
        elif choice == '4':
            show_all_info()
        elif choice == '5':
            purchase()
        elif choice == '6':
            goodbye()
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

# 6
def number_6():
    C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
    C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
    sum1 = 0
    sum2 = 0
    for i in C_1:
        sum1 += i
    for i in C_2:
        sum2 += i
    print(f"Даны 2 кортежа: {C_2} и {C_2}")
    print(f"Сумма больше в кортеже - {C_1 if sum1 > sum2 else C_2}")
    print(f"Номера минимальных элементов: {C_1.index(min(C_1)) + 1}, {C_2.index(min(C_2)) + 1}")
    print(f"Номера максимальных элементов: {C_1.index(max(C_1)) + 1}, {C_2.index(max(C_2)) + 1}")


number_1(1001)
number_2()
number_3()
number_35()
number_4()
number_5()
number_6()

