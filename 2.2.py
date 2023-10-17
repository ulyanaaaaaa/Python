import random

def foo(a):
    if isinstance(a, int):
        a = str(a)
        print(a[::-1])
    elif isinstance(a, tuple):
        print(f"Кортеж: {a}")
        print(len(a))
    elif isinstance(a, list):
        print(f"Список: {a}")
        sum = 0
        for num in a:
            if num == 0:
                break
            else:
                sum += num
        print(f'{sum} - сумма до нулевого элемента')
    elif isinstance(a, str):
        dict = {}
        max_count = 0
        for l in a:
            if l in dict:
                dict[l] += 1
            else:
                dict[l] = 1

        for l, count in dict.items():
            if count > max_count:
                max_count = count
                max_l = l
        print(f'Самый повторяющейся символ: {max_l}')

        a.strip()
        a = a.split()
        res = []
        for l in a:
            if l.strip():
                res.append(l)
        print(f'Количество слов в строке: {len(res)}')


try:
    foo(int(input("Введите целое число: ")))
except:
    print("Неверный ввод")

foo(tuple(random.randint(1, 10) for i in range(1, 11)))

foo(list(random.randint(1, 10) for i in range(1, 11)))

try:
    foo(str(input("Введите строку: ")))
except:
    print("Неверный ввод")


