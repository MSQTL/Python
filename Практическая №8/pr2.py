import random


def ex1():
    count = 0
    spisok = []
    while count < 8:
        spisok.append(int(input("Введите число: ")))
        count += 1

    print(f"Сумма: {sum(spisok)}, максимальное значение: {max(spisok)},"
          f" минимальное значение: {min(spisok)}")


#3ex1()


def ex2():
    def show(spisok):
        for i in range(len(spisok)):
            print(spisok[i], end=" ")
            if (i + 1) % 10 == 0:
                print("\n")

    count = 0
    spisok = []
    while count < 100:
        spisok.append(round(random.random() * 5, 2))
        count += 1

    show(spisok)
    print("Отсортированный список: ")
    spisok.sort()
    show(spisok)


#ex2()


def ex3():
    def show(spisok):
        for i in range(len(spisok)):
            if i % 2 == 0:
                print(spisok[i], end=" ")

    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(0, 20)))
        count += 1

    print(spisok)
    show(spisok)


ex3()


def ex4():
    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(0, 20)))
        count += 1
    print(spisok)

    for i in spisok:
        if int(i) % 2 == 0:
            print(i, end=" ")


#ex4()


def ex5():
    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(0, 20)))
        count += 1
    print(spisok)

    for i in range(len(spisok) - 1):
        if spisok[i] < spisok[i + 1]:
            print(spisok[i + 1], end=" ")


#ex5()


def ex6():
    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(-10, 10)))
        count += 1
    print(spisok)

    for i in range(len(spisok) - 1):
        if spisok[i] * spisok[i + 1] > 0:
            print(spisok[i], spisok[i + 1], end=" ")
            break


#ex6()


def ex7():
    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(150, 200)))
        count += 1
    print(spisok)

    spisok.sort()
    print(spisok)
    height = int(input("Рост Пети: "))
    # добавление Пети между
    for i in range(len(spisok) - 1):
        if int(spisok[i]) < height <= int(spisok[i + 1]):
            spisok.insert(i + 1, height)
            print(len(spisok) - i - 1)
            break
    # добавление Пети в конец
    if height <= spisok[0]:
        spisok.insert(0, height)
        print(len(spisok))
    # добавление Пети в начало
    elif height > spisok[len(spisok) - 1]:
        spisok.append(height)
        print(1)

    spisok.reverse()
    print(spisok)


#ex7()


def ex8():
    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(0, 10)))
        count += 1
    print(spisok)
    count = 0
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i] == spisok[j]:
                count += 1
    print(count)


#ex8()


def ex9():
    count = 0
    spisok = []
    while count < 10:
        spisok.append(round(random.randint(0, 10)))
        count += 1
    print(spisok)

    delete_index = int(input("Какой элемент удалить? "))
    spisok.pop(delete_index)

    print(spisok)


#ex9()
