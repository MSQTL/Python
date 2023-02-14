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
    
    
    
