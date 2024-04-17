/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    
    struct ListNode *ptr = head;

    if (head == NULL) {
        return head;
    } else {
        while (ptr->next != NULL) {
            if (ptr->val == ptr->next->val) {
                struct ListNode *toDelete = ptr->next;
                ptr->next = ptr->next->next;
                free(toDelete);
            } else {
                ptr = ptr->next;
            }
        }
    }

    return head;
}
