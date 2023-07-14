# Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []
    
    
    # Hash Table 01
   class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            numsMap = {}
            n = len(nums)
            
            # Build a hash table
            for i in range(n):
                numsMap[nums[i]] = i
                
            # Find Complement
            for i in range(n):
                complement = target - nums[i]
                if complement in numsMap and numsMap[complement] != i:
                    return [i, numsMap[complement]]
                
            return []
    # Hash Table 02
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            numsMap = {}
            n = len(nums)
            
            for i in range(n):
                complement = target-nums[i]
                if(complement in numsMap and numsMap[complement] != i):
                    return [numsMap[complement], i]
                numsMap[nums[i]] = i
                
            return []