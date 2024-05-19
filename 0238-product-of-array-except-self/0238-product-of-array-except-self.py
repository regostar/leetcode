class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # for num in nums:
        #     prod *= num
        # result = []
        # for num in nums:
        #     result.append(prod/num)
        #     # when it's 0, we need product of all elements before prod became zero because of this
        # return result
        
 
        
        result = [1 for _ in range(len(nums))]
        # now iterate to find each product
        prod_left = 1
        for i in range(1, len(nums)):
            result[i] = nums[i- 1] * prod_left
            prod_left *= nums[i- 1]

        prod_right = 1
        for i in range(len(nums)-2, -1, -1):
            result[i] *= nums[i+ 1] * prod_right
            prod_right *= nums[i+ 1]

        return result
            