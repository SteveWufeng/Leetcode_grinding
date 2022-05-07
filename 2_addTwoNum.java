/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // create a result ListNode default constructor
        ListNode result = new ListNode();
        // keep track of the head.
        ListNode head = result;
        
        // first loop through the l1 and add all val into the ListNode
        while (l1 != null) {
            result.val = l1.val;
            l1 = l1.next;
            if (l1 != null) {
                result.next = new ListNode();
                result = result.next;
            }
        }
        
        result = head; // return to head
        
        // second loop through l2 and add val into the result ListNode
        while (l2 != null) {
            result.val += l2.val;
            // increment l2 and result
            result = result.next;
            l2 = l2.next;
        }
        
        result = head;

        // for all elements >= 10 increment to the next result val
        // if the val is greater then 10
        while (result != null) {
            // current val minus 10
            if (result.val >= 10) {
                result.val -= 10;
                if (result.next == null) {
                    result.next = new ListNode(1);
                }
                else {
                    // add 1 to next node
                    result.next.val++;
                }
            }
            result = result.next;
        }
        
        // return head
        return head;
    }
}