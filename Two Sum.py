def two_sum(nums, target):
    table = {}
    for i, num in enumerate(nums):
        if target - num in table and table[target - num] != i:
            return [i, table[target - num]]

        table[num] = i

print(two_sum([2, 7, 11, 15], 9))
