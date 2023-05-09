class Solution:
    def twoSum(self,nums,target):
        required = {}
        for i in range(len(nums)):
            if target-nums[i] in required:
                return [required[target-nums[i]],i]
            else:
                required[nums[i]] = i
nums = [1,5,10,30,25,25]
target = 26
ob = Solution()
print(ob.twoSum(nums,target))