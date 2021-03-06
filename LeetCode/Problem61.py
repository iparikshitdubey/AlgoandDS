'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head

        length = 0
        while (node):
            length += 1
            node = node.next

        if k == 0:
            return head
        if length == 1:
            return head
        if length == 0:
            return

        x = k % length

        # node = head
        for i in range(x):
            node1, node2 = head, head
            val = 0
            while val < length - 2:
                node1 = node1.next
                node2 = node2.next
                val += 1
            node2 = node2.next
            node1.next = None
            node2.next = head
            head = node2
        return head