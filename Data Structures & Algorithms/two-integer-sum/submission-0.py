class Solution:
 def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Test Case 1
nums1 = [3, 4, 5, 6]
target1 = 7

sol = Solution()
print(sol.twoSum(nums1, target1))


# Test Case 2
nums2 = [4, 5, 6]
target2 = 10

print(sol.twoSum(nums2, target2))