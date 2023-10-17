def is_anagram(first, second):
    if(sorted(first) == sorted(second)):
        print("Анограмма")
    else:
        print("Не анограмма")

try:
    first = input(str("Введите первое слово: "))
    second = input(str("Введите второе слово: "))
    if (first.isalpha() and second.isalpha()):
        is_anagram(first, second)
    else:
        print("Введите корректные слова")
except:
    print("Введите корректные слова")



    