/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode *slow = head, *fast = head;
    struct ListNode *prev = NULL, *temp;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    while (slow) {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    slow = prev;
    fast = head;

    while (slow) {
        if (fast->val != slow->val) {
            return false;
        }
        fast = fast->next;
        slow = slow->next;
    }
    return true;
}
