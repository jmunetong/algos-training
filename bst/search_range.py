class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self._get_index(nums, target, 0, len(nums)-1, True), self._get_index(nums, target, 0, len(nums)-1, False)]

    def _get_index(self, nums, target, start, end, lower):

        low, high = start, end
        idx = -1
        
        while low <= high:
            mid = low + (high - low  + 1) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                idx = mid
                if lower:
                    high = mid - 1
                else: 
                    low = mid + 1

        return idx


        