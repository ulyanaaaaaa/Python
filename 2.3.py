def massive():
    try:
        r=int(input("Введите размер массива: "))
        mas = [list(map(int,input("Введите элементы массива: ").split()))for i in range(r)]
        # mas = [list(map(int, input("Введите элементы массива: ").split())) for i in range(r)]
    except:
        print("Введены неккоректные данные")
        return
    print(mas)
    max_value = mas[0][0]
    max_row = 0
    max_col = 0
    for row in range(len(mas)):
        for col in range(len(mas[row])):
            if mas[row][col] > max_value:
                max_value = mas[row][col]
                max_row = row
                max_col = col

    print("Индексы первого вхождения максимального элемента:")
    print("Номер строки:", max_row + 1)
    print("Номер столбца:", max_col + 1)

massive()


