class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        
        ListNode * curr = head;
        ListNode * temp = curr;

        if(head != NULL && head->next == NULL) return head;

        while(curr != NULL)
        {
            if(curr->next != NULL && (curr->val == curr->next->val))
            {
                curr->next = curr->next->next;
            }
            else curr = curr->next;

        }

    return temp;
    }
};
