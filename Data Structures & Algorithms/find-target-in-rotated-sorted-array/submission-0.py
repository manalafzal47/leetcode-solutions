class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize l and r
        l=0
        r=len(nums)-1
    
        while l <= r:
            mid = (l+r) // 2

            # check if nums[mid] == target
            if nums[mid] == target:
                return mid

            # check if left half is sorted. 
            # target is in left half
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                
                # else, discard the left half
                else:
                    l = mid+1

            # target is in right half
            else:
                # check if target is within the right half.
                if nums[mid] < target <= nums[r]:
                    l = mid+1

                #else, discard the left half
                else:
                    r = mid-1
        return -1
