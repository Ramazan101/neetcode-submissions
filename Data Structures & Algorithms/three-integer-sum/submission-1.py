class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, n in enumerate(nums):
            if i != 0 and n == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            target = -n

            while l < r:
                if nums[l]+nums[r] > target:
                    
                    r-=1
                elif nums[l]+nums[r] < target:
                    l+=1
                else:
                    if [n, nums[l], nums[r]] not in res:
                        res.append([n, nums[l], nums[r]])
                    r-=1
                    l+=1
            
        return res