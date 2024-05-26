#
# 创建链表统一格式：
# dummy = Listnode(0) current = dummy current.next = Listnode()
# 考虑进位和结果

#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 结果链表
        head = ListNode(0)
        # 头节点
        current = head
        ## 进位
        carry = 0

        # 只要有一个链表不为空都进入循环
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            total = x + y + carry
            carry = total // 10
            ## 创建结果链表，把最末尾的结果存储
            current.next = ListNode(total % 10)

            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # 剩余的进位
        if carry > 0:
            current.next = ListNode(carry)

        return head.next

def create_list(nums):
    dummy = ListNode(0)
    current = dummy
    for item in nums:
        current.next = ListNode(item)
        current = current.next
    return dummy.next

def print_linked_list(node):
    while node is not None:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# 测试
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print_linked_list(result)