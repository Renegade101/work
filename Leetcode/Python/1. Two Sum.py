class Solution(object):
    nums = [2, 7, 11, 15]
    target = 9
    def twoSum(nums, target):
        m = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in m:
                return [m[diff], n]
            else:
                m[nums[n]] = n

    print(twoSum(nums, target))
