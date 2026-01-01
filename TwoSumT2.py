class Solution(object):
    def findPairModZero(self, nums, target):
        i=0
        while i < len(nums):
            j = i + 1
            while j < len(nums):

                # special case when target == 0
                if target == 0:
                    if nums[i] + nums[j] == 0:
                        return [i, j]
                else:
                    if (nums[i] + nums[j]) % target == 0:
                        return [i, j]

                j += 1
            i += 1
        return []