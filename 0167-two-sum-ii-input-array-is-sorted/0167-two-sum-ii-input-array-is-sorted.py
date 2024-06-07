class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointers, one at start, other at end
        # compute sum start and end
        # if less than target then move start 
        # if greater than target then move left
        start = 0
        end = len(numbers) - 1
        while start < end:
            tot = numbers[start] + numbers[end]
            if tot == target:
                # found
                return [start + 1, end + 1]
            if tot < target:
                start += 1
            elif tot > target:
                end -= 1
        
        