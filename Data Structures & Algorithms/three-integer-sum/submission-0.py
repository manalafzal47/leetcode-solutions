class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                return res
            if i and num == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                if (cur_sum := num + nums[l] + nums[r]) == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1

        return res