public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {val = x;}
}



// Iterative
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
}

// Recursive
public class Solution {
    public ListNode reverseList(ListNode head) {
        return reverseListHelper(head, null);
    }

    private ListNode reverseListHelper(ListNode head, ListNode newHead) {
        if (head == null)
            return newHead;

        ListNode next = head.next;
        head.next = newHead;
        return reverseListHelper(next, head);
    }
}