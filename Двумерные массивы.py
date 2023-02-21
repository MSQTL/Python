def main():
    ex2()


def ex1():
    size = [int(j) for j in input().split()]

    n = size[0]
    m = size[1]

    a = [[int(j) for j in input().split()] for i in range(n)]
    max = a[0][0]
    maxI = 0
    maxJ = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > max:
                max = a[i][j]
                maxI = i
                maxJ = j

    print(maxI, maxJ)


def ex2():
    n = int(input())

    mass = ['.'] * n
    for i in range(n):
        mass[i] = ['.'] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                mass[i][j] = '*'
            if i == j:
                mass[i][n - j - 1] = '*'
            if i == n // 2:
                mass[i][j] = '*'
            if j == n // 2:
                mass[i][j] = '*'

    for row in mass:
        for item in row:
            print(item, end=" ")
        print("\n")


def ex3():
    n, m = [int(i) for i in input().split()]

    mass = []
    for i in range(n):
        mass.append([])
        for j in range(m):
            if (i + j) % 2 == 0:
                mass[i].append('.')
            else:
                mass[i].append('*')

    for row in mass:
        for item in row:
            print(item, end=" ")
        print("\n")


def ex4():
    n = int(input())

    mass = [0] * n
    for i in range(n):
        mass[i] = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            mass[i][j] = abs(j - i)

    for row in mass:
        for item in row:
            print(item, end=" ")
        print("\n")


def ex5():
    n = int(input())

    mass = [0] * n
    for i in range(n):
        mass[i] = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                mass[i][n - j - 1] = 1
            if n - i - 1 < j:
                mass[i][j] = 2

    for row in mass:
        for item in row:
            print(item, end=" ")
        print("\n")


def ex6():
    n, m = [int(i) for i in input().split()]

    mass = [[int(j) for j in input().split()] for i in range(n)]

    a, b = [int(i) for i in input().split()]

    aList = []
    bList = []
    for i in range(n):
        bList.append(mass[i][b])
        aList.append(mass[i][a])
    for i in range(n):
        mass[i][a] = bList[i]
        mass[i][b] = aList[i]

    for row in mass:
        for item in row:
            print(item, end=" ")
        print("\n")


main()
