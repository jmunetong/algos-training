class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}
        for idx, num in enumerate(nums):
            if target-num in vals:
                return [vals[target-num], idx]
            vals[num] = idx

## To sum with pointers:
def two_sum_problem(target, nums):
    nums.sort()
    left = 0
    right= len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [nums[left], nums[right]]
        elif nums[left] + nums[right] >  target:
            right -= 1
        else:
            left
    return []

assert two_sum_problem(9, [2, 7, 11, 15]) == [2, 7]
        
