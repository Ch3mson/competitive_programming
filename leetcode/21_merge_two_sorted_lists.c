/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL && list2 == NULL) {
        return NULL;
    } else if (list1 == NULL) {
        return list2;
    } else if (list2 == NULL) {
        return list1;
    }

    struct ListNode *output = malloc(sizeof(struct ListNode));

    if (list1->val < list2->val) { // insert list1
        output->val = list1->val;
        list1 = list1->next;
    } else {
        output->val = list2->val;
        list2 = list2->next;
    }

    struct ListNode *iter = output; // iter itterates, while output points at front

    while (list1 != NULL && list2 != NULL) {
        iter->next = malloc(sizeof(struct ListNode));
        iter = iter->next;

        if (list1->val < list2->val) {
            iter->val = list1->val;
            list1 = list1->next;
        } else {
            iter->val = list2->val;
            list2 = list2->next;
        }
    }

    if (list1 == NULL && list2 != NULL) {
        while (list2 != NULL) {
            iter->next = malloc(sizeof(struct ListNode));
            iter = iter->next;

            iter->val = list2->val;
            list2 = list2->next;
        }
    } else if (list1 != NULL && list2 == NULL) {
        while (list1 != NULL) {
            iter->next = malloc(sizeof(struct ListNode));
            iter = iter->next;

            iter->val = list1->val;
            list1 = list1->next;
        }
    }

    iter->next = NULL;
    return output;
}
