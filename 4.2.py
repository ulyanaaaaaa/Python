def calculate_wall_area(length, width, height, windows, doors):

    wall_area = 2 * (length + width) * height

    for window in windows:
        window_area = window[0] * window[1]
        wall_area -= window_area

    for door in doors:
        door_area = door[0] * door[1]
        wall_area -= door_area
    return wall_area

try:
    length = float(input("Введите длину стены (в метрах): "))
except:
    print("Неверный ввод данных!")
try:
    width = float(input("Введите ширину стены (в метрах): "))
except:
    print("Неверный ввод данных!")
try:
    height = float(input("Введите высоту стены (в метрах): "))
except:
    print("Неверный ввод данных!")


windows = []
try:
    num_windows = int(input("Введите количество окон: "))
except:
    print("Неверный ввод данных!")
for i in range(num_windows):
    try:
        window_width = float(input("Введите ширину окна №{} (в метрах): ".format(i+1)))
    except:
        print("Неверный ввод данных!")
    try:
        window_height = float(input("Введите высоту окна №{} (в метрах): ".format(i+1)))
    except:
        print("Неверный ввод данных!")
    windows.append((window_width, window_height))

doors = []
try:
    num_doors = int(input("Введите количество дверей: "))
except:
    print("Неверный ввод данных!")
for i in range(num_doors):
    try:
        door_width = float(input("Введите ширину двери №{} (в метрах): ".format(i+1)))
    except:
        print("Неверный ввод данных!")
    try:
        door_height = float(input("Введите высоту двери №{} (в метрах): ".format(i+1)))
    except:
        print("Неверный ввод данных!")
    doors.append((door_width, door_height))

total_wall_area = calculate_wall_area(length, width, height, windows, doors)
print("Общая площадь стены для оклеивания обоями:", total_wall_area)