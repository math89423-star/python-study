"""
题目：两数之和
描述：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案

进阶：
你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
"""

# 解法一：通过
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         result = []
#         index1 = 0
#         for num1 in nums:
#             index2 = index1 + 1
#             for num2 in nums[index1 + 1:]:
#                 if num1 + num2 == target:
#                     result.append(index1)
#                     result.append(index2)
#                     return result
#                 index2 += 1
#             index1 += 1
#         return result
        
# 解法二：哈希表（时间复杂度O(n)）
"""
解法描述：
使用空间换时间的策略，核心思路：利用哈希表（Python中就是字典Dict）
核心逻辑：在遍历数组时，在当前的数字num之前，是否已经出现了另一个数字num2 = target -num
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []




if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    res = []
    solution = Solution()
    res = Solution.twoSum(res, nums, target)
    print(res)

