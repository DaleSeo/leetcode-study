/*
    풀이 :
        list를 vector에 저장한 뒤 끝에서 n - 1 번째 노드->next를 n번째 노드->next로 치환

    노드 개수 : N

    TC : O (N)

    SC : O (N)
*/

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
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            ListNode*   tmp = head;
            vector<ListNode*>   list;
    
            while (tmp) {
                list.push_back(tmp);
                tmp = tmp->next;
            }
            int idx = list.size() - n;
            if (idx == 0)
                return head->next;
            else {
                list[idx - 1]->next = list[idx]->next;
                return head;
            }
        }
    };
