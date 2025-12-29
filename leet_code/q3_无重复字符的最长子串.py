"""
Docstring for leet_code.q3_无重复字符的最长子串
题目：无重复字符的最长子串
描述：
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
示例：
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。

示例：
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例：
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

# # 解法一：
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_len = len(s)
#         index = 0
#         count = 0
#         sub_str = ""
#         max_sub_str = ""
#         while count < max_len:
#             index = count
#             while index < max_len:
#             # 假如原来的子串中没有这个字符，则增加原来的子串长度
#                 if sub_str.count(s[index]) == 0:
#                     sub_str += s[index]
#                     print(f"sub_str:{sub_str}")
#                 # 遇到重复，比较是否是当前最长的子串, 清空字符串从count+1重新开始字符串
#                 else:
#                     if len(sub_str) > len(max_sub_str):
#                         max_sub_str = sub_str
#                         # 清空原来的子串，重新开始子串计数
#                         sub_str = ""
#                         sub_str += s[count]
#                     else:
#                         # 不进行最长子串替换，清空原来的子串，重新开始子串计数
#                         sub_str = ""
#                         sub_str += s[count]
#                     count += 1
#                     break
#                 # 更新最大子串
#                 if len(sub_str) > len(max_sub_str):
#                     max_sub_str = sub_str
#                 index += 1
#         return len(max_sub_str)


# 解法二：使用滑动窗口 + 哈希表 优化
"""
核心思路：
1. 维护一个窗口[left, right]，保证窗口内的字符都不重复。
2. 使用一个字典 char_map 记录字符 上一次出现的索引位置。
3. 遍历字符串（移动 right 指针）：
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 哈希表，记录字符及其最新出现的索引 {字符: 索引}
        char_map = {}
        # 滑动窗口左边界
        left = 0
        # 最大长度
        max_len = 0

        # right 为滑动窗口右边界，从 0 开始遍历
        for right in range(len(s)):
            current_char = s[right]

            # 如果字符已经在字典中，且该字符上一次出现的位置在当前窗口内 (>= left)
            # 说明发现了重复字符，需要收缩窗口
            if current_char in char_map and char_map[current_char] >= left:
                # 直接将左边界跳到重复字符上一次出现位置的下一位
                # 例如 "dvdf"，当遍历到第二个 'd' (index 2) 时，left 直接从 0 跳到 1 (即 'v' 的位置)
                left = char_map[current_char] + 1
            
            # 无论是否重复，都更新当前字符的最新索引位置
            char_map[current_char] = right
            
            # 计算当前无重复子串的长度，并尝试更新最大值
            # 长度计算公式：右边界 - 左边界 + 1
            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == '__main__':
    full_str = "abcdaaaaabc"
    solution = Solution()
    sub_str_len = solution.lengthOfLongestSubstring(full_str)
    print(f"sub_str_len:{sub_str_len}")