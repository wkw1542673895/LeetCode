from typing import List


class Solution:

    def twoSum(self, nums, target):
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [i, keys[target - nums[i]]]
            elif nums[i] not in keys:
                keys[nums[i]] = i

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low += 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                elif sum > 0:
                    high -= 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

        return result


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
re = s.threeSum(nums)
print(re)
