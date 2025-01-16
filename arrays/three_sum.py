class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i -1] != nums[i]:
                self.twoSum(list_result, i, nums)
        return list_result

    def twoSum(self, list_result, i, nums):
        num_tracker = set()
        j = i +1
        while j < len(nums):
            current = - nums[i] - nums[j]
            if current in num_tracker:
                candidate_group = [current, nums[i], nums[j]]
                candidate_group.sort(
                )
                list_result.append(candidate_group)
                while j < len(nums) -1 and nums[j] == nums[j+1]:
                    j += 1
            num_tracker.add(nums[j])
            j += 1

