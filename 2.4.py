def foo1():
    try:
        number = int(input("Введите целое число"))
        print(number)
    except:
        print("Введено не число")
    finally:
        print("Завершение программы try")

foo1()