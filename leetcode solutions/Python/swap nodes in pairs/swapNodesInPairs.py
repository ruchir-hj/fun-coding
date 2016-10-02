class ListNode(object):
    def __init__(self, x):
        self.val
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            nextOne = curr.next
            nextTwo = curr.next.next
            nextThree = curr.next.next.next

            curr.next = nextTwo
            nextTwo.next = nextOne
            nextOne.next = nextThree
            curr = nextOne

        return dummy.next