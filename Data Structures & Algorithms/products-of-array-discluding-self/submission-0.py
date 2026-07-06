class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answr = [1] * (len(nums))

        pre = 1
        for i in range(len(nums)):
            answr[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            answr[i] *= post
            post *= nums[i]

        return answr