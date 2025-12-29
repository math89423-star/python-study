"""
Docstring for leet_code.q2_两数相加
题目：两数相加
描述：
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例：
输入：l1 = [0], l2 = [0]
输出：[0]

示例：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
* 每个链表中的节点数在范围 [1, 100] 内
* 0 <= Node.val <= 9
* 题目数据保证列表表示的数字不含前导零
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        add_num1 = self.caculate_add_sum(l1)
        add_num2 = self.caculate_add_sum(l2)
        #print(f"add_num1:{add_num1}  add_num2:{add_num2}")
        sum = add_num1 + add_num2
        #print(f"sum:{sum}")
        # 求余数做数组
        if sum == 0:
            res_link = ListNode(0)
            return res_link
        res = []
        while sum != 0:
            res.append(sum % 10)    # 百分号%是取余数
            sum = sum // 10         # //代表整除
            res_link = self.create_linked_list(res)
        return res_link
    
    def create_linked_list(self, arr):
        # 定义哑结点，便于链表操作
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            # 每读到一个数字，就建立一个节点
            current.next = ListNode(val)
            # 指针向后移动一步，站在新节点
            current = current.next
        # dummy是虚假的链表头，dummy.next才是真正的链表头
        return dummy.next

    def print_linked_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def caculate_add_sum(self, caculate_list):
        # TODO:取值，取值系数，加数
            current = caculate_list
            sum = 0     # 求加数1的值，起始值为0
            sqar_num = 1    # 代表乘积系数，头结点是1，后面一个节点依次扩大10倍
            while current:
                # num代表当前位数值
                num = current.val
                current = current.next
                add_num = num * sqar_num
                sum += add_num
                sqar_num *= 10
            return sum

if __name__ == '__main__':
    arr1 = [0]
    arr2 = [0]
    solution = Solution()
    l1 = solution.create_linked_list(arr1)
    l2 = solution.create_linked_list(arr2)
    res = solution.addTwoNumbers(l1, l2)

    print(solution.print_linked_list(res))