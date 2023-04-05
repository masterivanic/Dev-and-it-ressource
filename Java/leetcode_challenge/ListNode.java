package Java.leetcode_challenge;

public class ListNode {

    int val;
    ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public ListNode removeNode(ListNode node, int value) {
        if(node.next != null) {
            if(node.val == value) {
               node = null;
            }
        }
        return node;
    }
}

