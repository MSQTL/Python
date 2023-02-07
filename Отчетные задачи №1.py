def main():
    ex6()


def ex1():
    a = int(input("Сколько рублей стоит пирожок? "))
    b = int(input("Сколько копеек стоит пирожок? "))
    n = int(input("Сколько пирожков Вы хотите купить? "))

    itogRub = a * n + (b * n) // 100
    itogKop = (b * n) % 100

    print(f"За {n} пирожков(-ка) нужно заплатить {itogRub} рублей(-ля) и {itogKop} копеек(-ки).")


def ex2():
    h1 = int(input("Введите любой момент времени в часах: "))
    h2 = int(input("Введите любой момент времени в часах: "))

    m1 = int(input("Введите любой момент времени в минутах: "))
    m2 = int(input("Введите любой момент времени в минутах: "))

    s1 = int(input("Введите любой момент времени в секундах: "))
    s2 = int(input("Введите любой момент времени в секундах: "))

    resultH = (h2-h1) * 3600
    resultM = m2-m1 * 60
    resultS = s2-s1
    result = resultH + resultM + resultS

    print("Между этим промежутком времени прошло ", result, " секунд")


def ex3():
    number = int(input("Сколько всего карточек? "))
    summ = 0
    for i in range(1, number + 1):
        summ += i

    for i in range(1, number):
        summ -= int(input("Введите номер оставшейся карточки: "))

    print(f"Номер потеряшки: {summ}")


def ex4():
    str = "qwertyuiop"
    result = ""
    for i in str:
        if str.index(i) % 3 == 0:
            continue
        result += i
    print(f"Полученная строка: {result}")


def ex5():
    str = "ahhhhhhhhhhha"
    fh = str.find('h')
    lh = str.rfind('h')
    result = ""
    for i in range(len(str)):
        if str[i] == 'h':
            if i != fh and i != lh:
                result += 'H'
            else:
                result += str[i]
        else:
            result += str[i]
    print(result)


def ex7():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите действие над числами: ")
    match operation:
        case '+':
            print(f"{num1} + {num2} = ",num1 + num2)
        case '-':
            print(f"{num1} - {num2} = ",num1 - num2)
        case '*':
            print(f"{num1} * {num2} = ", num1 * num2)
        case '/':
            if(num2 != 0):
                print(f"{num1}/{num2} = ", num1 / num2)
            else:
                print("Деление на 0!")
        case 'mod':
            print(f"{num1} mod {num2} = ", num1 % num2)
        case 'pow':
            print(f"{num1} pow {num2} = ", pow(num1, num2))
        case 'div':
            print(f"{num1} div {num2} = ", (num1 // num2))


def ex6():
    lst = list()
    ulist = list()
    while(True):
        ulist.append(int(input("Введите число: ")))
        if ulist[-1] == 0:
            ulist.remove(0)
            break
    lst.append(ulist)
    lst.append(int(input("Введите число, которое хотите найти: ")))

    print(f"Полученный список чисел: {lst[0]}")
    count = 0
    for i in range(len(lst[0])):
        if lst[0][i] == lst[1]:
            count += 1
            print(f"Индекс числа {lst[1]}: {i}")
    if count == 0:
        print(f"Число {lst[1]} отсутствует!")


def ex8():
    count = int(input("Сколько студентов находится в аудитории? "))
    if(count % 10 == 0 or (count % 10 >= 5 and count % 10 <= 9)):
        print(f"{count} программистов")
    if(count % 10 == 1):
        if(count % 100 >= 11 and count % 100 <= 14):
            print(f"{count} программистов")
        else:
            print(f"{count} программист")
    if(count % 10 >= 2 and count % 10 <= 4):
        if(count % 100 >= 12 and count % 100 <= 14):
            print(f"{count} программистов")
        else:
            print(f"{count} программиста")


main()
