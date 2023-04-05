
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
package Java.leetcode_challenge;

import java.util.LinkedList;

public class Solution {


    public static LinkedList<Integer> list = new LinkedList<>();
    public static LinkedList<ListNode> listNode = new LinkedList<>();
    
    public static LinkedList<Integer> getLinkedList(ListNode node) {
        if (node instanceof ListNode) {
            if (node.next != null) {
                list.add(node.val);
                getLinkedList(node.next);
            } else {
                list.add(node.val);
            }
        }
        return list;
    }
    
    public static LinkedList<ListNode> getLinkedListNode(ListNode node) {
        if (node instanceof ListNode) {
            if (node.next != null) {
                listNode.add(node);
                getLinkedListNode(node.next);
            } else {
                list.add(node.val);
            }
        }
        return listNode;
    }

    public static void main(String[] args) {
        ListNode node = new ListNode(1, new ListNode(3, new ListNode(4, new ListNode(7, 
                new ListNode(1, new ListNode(2 , new ListNode(6)))))));
        ListNode node1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        ListNode node2 = new ListNode(2, new ListNode(1));

        LinkedList<ListNode> value = Solution.getLinkedListNode(node2);
        System.out.println("-------- linkedList:: --------" + value);
        int partMove = value.size()/2;
        System.out.println("---- middle of list-----: " + partMove);
        value.remove(partMove);
        System.out.println("After removing we have::::: " + value);
       
    }
}
