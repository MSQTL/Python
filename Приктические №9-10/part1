import random


def ex1():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = list_1.copy()

    list_2[2] = 0

    print(list_1)
    print(list_2)


# ex1()


def ex2():
    def create(start, end):
        list_1 = []
        for i in range(10):
            list_1.append(random.randint(start, end))
        return tuple(list_1)

    tuple_1 = create(0, 5)
    tuple_2 = create(-5, 0)
    tuple_3 = tuple_1 + tuple_2

    print(tuple_3)
    print(tuple_3.count(0))


ex2()
