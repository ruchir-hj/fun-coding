class ListNode(object):
    def __init__(self):
        self.val = x
        self.next = None


# Iterative

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



# recursive

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseListHelper(head, None)

    def reverseListHelper(self, node, prev=None):
        if not node:
            return prev

        nextNode = node.next
        node.next = prev
        return self.reverseListHelper(nextNode, node)

