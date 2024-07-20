def third_max(nums):
    nums = list(set(nums))
    nums.sort(reverse=True)
    return nums[2] if len(nums) >= 3 else nums[0]
print(third_max([3, 2, 1, 4]))
