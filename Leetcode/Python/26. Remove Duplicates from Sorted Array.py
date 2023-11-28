class Solution(object):
    nums = [0,0,1,1,1,2,2,3,3,4]
    def removeDuplicates(nums):
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count
    print(removeDuplicates(nums))