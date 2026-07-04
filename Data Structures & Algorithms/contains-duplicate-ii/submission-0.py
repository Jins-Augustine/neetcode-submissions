class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i=0
        for r in range(len(nums)):
            if r-i > k:
                window.remove(nums[i])
                i += 1

            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
        