struct ListNode {
    int val;
    ListNode *next;
    ListNode (int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {

        if ((head == NULL) || (head->next == NULL)) {
            return head;
        }

        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *curr = dummy;
        ListNode *nextOne = NULL;
        ListNode *nextTwo = NULL;
        ListNode *nextThree = NULL;

        while (curr->next != NULL && curr->next->next != NULL) {
            nextOne = curr->next;
            nextTwo = curr->next->next;
            nextThree = curr->next->next->next;

            curr->next = nextTwo;
            nextTwo->next = nextOne;
            nextOne->next = nextThree;

            curr = nextOne;
        }
        return dummy->next;
    }
};