def ex1():
    old_names = ["one", "two", "three", "four", "five"]
    new_names = ["один", "два", "три", "четыре", "пять"]
    file = open("data.txt")
    new_file = open("new_data.txt", "w", encoding="utf-8")

    text = file.read()
    print(text)
    for i in range(len(old_names)):
        if old_names[i] in text:
            text = text.replace(old_names[i], new_names[i])

    print(text)
    new_file.write(text)

    file.close()
    new_file.close()


# ex1()


def ex2():
    file = open("nums.txt")
    summ = 0
    for i in file.read().split():
        summ += int(i)
    print(summ)


ex2()
