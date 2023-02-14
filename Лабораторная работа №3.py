def ex1():
    list_num = list(map(int, input().split()))

    answer = []

    if len(list_num) == 1:
        print(*list_num)
    else:
        for index, value in enumerate(list_num):
            if index != len(list_num) - 1:
                answer.append(list_num[index-1] + list_num[index+1])
            else:
                answer.append(list_num[index-1] + list_num[0])
        print(*answer)

#ex1()

def ex2():
    nums = list()
    count = int(input("Введите количство чисел в списке: "))
    for i in range(count):
        nums.append(int(input("Введите число: ")))

    print(nums)

    repeatNums = list()

    for item in nums:
        if nums.count(item) > 1:
            if repeatNums.count(item) == 0:
                repeatNums.append(item)

    print(repeatNums)

    length = len(nums)
    for i in range(length):
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    print(nums)

    
def ex3():
    nums = list()
    sum = 0

    while True:
        num = int(input("Введите число: "))
        sum += num
        if sum == 0:
            nums.append(num)
            break
        else:
            nums.append(num)
    sum = 0
    for i in nums:
        sum += i*i
    print(sum)
    
    
def ex5():
    words_count = int(input())
    words_set = set(input().lower() for i in range(words_count))

    lines_count = int(input())

    unique_words = set()
    for i in range(lines_count):
        line = input().lower().split()
        for word in line:
            if word not in words_set:
                unique_words.add(word)

    for word in unique_words:
        print(word)

ex5()
    
def ex6(password):
    special_characters = "!@#$%^&*()-+"

    answer = 0

    if not any(char.isdigit() for char in password):
        answer += 1
    if not any(char.islower() for char in password):
        answer += 1
    if not any(char.isupper() for char in password):
        answer += 1
    if not any(char in special_characters for char in password):
        answer += 1

    missing_length = max(0, 6 - len(password))

    return max(answer, missing_length)

password = input()
print(ex6(password))
