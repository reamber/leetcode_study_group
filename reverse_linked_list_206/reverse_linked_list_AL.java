public ListNode reverseList(ListNode head) {
        
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode prev = null;
        while(head != null){
            ListNode next = head.next; //first store the next node because you won't have this connection later
            head.next = prev; //reverse it
            prev = head;
            head = next;
        }
        return prev;
        
    }
