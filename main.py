def ex1():
    students = ["Соня", "Маша", "Серёжа", "Даша", "Саша", "Петя", "Тимофей"]
    print(students)
    print(students[0:2])


def ex2():
    students = ["Соня", "Маша", "Серёжа", "Даша", "Саша", "Петя", "Тимофей"]
    print(students)
    result = ""
    for name in students:
        if students.index(name) % 2 == 0:
            result += name + " "
    print(result)


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

ex5()
