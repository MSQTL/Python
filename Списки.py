"""
Выведите все элементы списка с четными индексами
"""


def ex1():
    students = ["Соня", "Маша", "Серёжа", "Даша", "Саша", "Петя", "Тимофей"]
    print(students)
    print(students[0:2])


"""
Выведите все четные элементы списка.
При этом используйте цикл for, перебирающий элементы спика, а не их индексы!
"""


def ex2():
    students = ["Соня", "Маша", "Серёжа", "Даша", "Саша", "Петя", "Тимофей"]
    print(students)
    result = ""
    for name in students:
        if students.index(name) % 2 == 0:
            result += name + " "
    print(result)


"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних чисел одного знака нет - не выводите ничего.
Если таких пар соседей несколько - выведите первую пару
"""


def ex3():
    nums = list()
    while (True):
        nums.append(int(input("Введите число: ")))
        if nums[-1] == 0:
            nums.remove(0)
            break
    print(nums)

    i = 1
    while i <= len(nums):
        if nums[i] * nums[i - 1] > 0:
            print(nums[i - 1], nums[i])
            break
        i += 1


"""
Переставьте соседние элементы списка местами.
"""


def ex4():
    nums = list()
    while (True):
        nums.append(int(input("Введите число: ")))
        if nums[-1] == 0:
            nums.remove(0)
            break
    i = 1
    while i < len(nums):
        num = nums[i]
        nums[i] = nums[i - 1]
        nums[i - 1] = num
        i += 2
    print(nums)


"""
В списке все элементы различны.
Поменятйте местами минимальный и максимальный элемент этого списка
"""


def ex5():
    objects = list()
    while (True):
        objects.append(input("Введите значение: "))
        if objects[-1] == "0":
            objects.remove("0")
            break
    print(objects)

    min = objects[0]
    max = objects[0]
    for item in objects:
        if min > item:
            min = item
        if max < item:
            max = item

    indexMin = objects.index(min)
    indexMax = objects.index(max)
    objects[indexMax] = min
    objects[indexMin] = max

    print(objects)
