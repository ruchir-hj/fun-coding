public class ListNode {
    int val;
    ListNode next;
    ListNode (int x) {val = x;}
}

public class Solution {
    public ListNode swapPairs(ListNode head) {

        if ((head == null) || (head.next == null)) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        ListNode nextOne = null;
        ListNode nextTwo = null;
        ListNode nextThree = null;

        while (curr.next != null && curr.next.next != null) {
             nextOne = curr.next;
             nextTwo = curr.next.next;
             nextThree = curr.next.next.next;

             curr.next = nextTwo;
             nextTwo.next = nextOne;
             nextOne.next = nextThree;

             curr = nextOne;
        }
        return dummy.next;

    }
}