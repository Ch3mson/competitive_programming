/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr;
        ListNode *front = head;
        ListNode *tmp = head;
        while (front != nullptr) {
            tmp = tmp->next;
            front->next = prev;
            prev = front;
            front = tmp;
        }
        return prev;
    }
};
