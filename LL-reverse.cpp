class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        ListNode * A = NULL;
        ListNode * temp;
        
        while (head != NULL)
        {
            temp = head->next;
            head->next = A;
            A = head;
            head = temp;   
            
        }
        
        return A;
        
    }
};
