def sum_nums(nums, target):
    for i in range(len(nums)):
        for num in range(i+1, len(nums)):
            if nums[i] + nums[num] == target:
                return print([i, num])
    return print('Таких чисел нет!')

sum_nums([1, 2, 3, 4], 6)