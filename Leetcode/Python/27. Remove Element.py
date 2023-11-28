class Solution(object):
    nums = [3,2,2,3]
    val = 3
    def removeElement(nums, val):
        nums[:] = (value for value in nums if value != val)
        return len(nums)
    print(removeElement(nums, val))