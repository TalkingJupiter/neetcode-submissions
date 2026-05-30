class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i>= len(sorted_nums)-1:
                return False
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False
