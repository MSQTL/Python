import random


def ex1():
    print(random.randrange(6, 12))
    print(random.randrange(5, 100, 5))


ex1()


def ex2():
    start, end = map(int, input("Границы: ").split())
    choice = 1 if input("1 - int, 2 - float ") == "1" else 2
    match choice:
        case 1:
            print(random.randrange(start, end))
        case 2:
            print(float(random.random() * (end - start) + start))


ex2()


def randomizer(start, end):
    return random.randrange(start, end)


print(f"Случайное число: {randomizer(1, 9)}")


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(11))


def ex5():
    nums = (4, 2, 8, 6, 0)

    def reverse(nums):
        print(nums[-1], end=" ")
        if len(nums) >= 2:
            reverse(nums[0: len(nums) - 1])

    reverse(nums)


ex5()


def ex6():
    population = [100, 120, 130, 99, 93, 73, 113, 119, 84, 56, 111, 154]
    area = [56, 98, 100, 78, 84, 99, 86, 101, 54, 76, 90, 127]
    print(sum([x / y for x, y in zip(population, area)])/len(population))


ex6()
