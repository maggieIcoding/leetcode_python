# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return([i, j])
            else:
                pass


nums = [3,3]
target = 6

out = two_sum(nums, target)
print(out)