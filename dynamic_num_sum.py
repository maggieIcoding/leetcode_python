# 输入：nums = [1,2,3,4]
# 输出：[1,3,6,10]
# 解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 

# output_list = []
# def runningSum(nums):
#     output_list.append(nums[0])
#     for i in range(1, len(nums)+1):
#         output_list.append(nums[i] + nums[i-1])
#     return(output_list)

# nums = [1,2,3,4]
# ret = runningSum(nums)
# print(ret)

class Solution(object):

    
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

nums = [1,2,3,4]
a = Solution()
print(a.runningSum(nums))