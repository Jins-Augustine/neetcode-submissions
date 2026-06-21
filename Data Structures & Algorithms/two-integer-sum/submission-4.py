class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}

        for i in range(len(nums)):
            s = target-nums[i]
            if s in seen:
                return [seen[s],i]
            else:
                seen[nums[i]]=i
        