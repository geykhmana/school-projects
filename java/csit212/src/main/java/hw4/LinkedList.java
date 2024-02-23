package hw4;

public class LinkedList {
	
	public ListNode head;
	
	public LinkedList () {
		head = null;
	}
	
	/*
	 * Implement the LIST-SEARCH(L, k) function
	 */
	public ListNode search (int k) {
		ListNode x = head;

		while (x != null && x.key != k) {
			x = x.next;
		}

		return x;
	}
	
	/*
	 * Implement the LIST-INSERT(L, x) function
	 * Note that x is an integer value, not a ListNode
	 */
	public void insert (int x) {
		ListNode lnx = new ListNode(x);
		lnx.next = head;

		if (head != null) {
			head.prev = lnx;
		}

		head = lnx;
		lnx.prev = null;
	}
	
	/*
	 * Implement the LIST-DELETE(L, x) function
	 */
	public void delete (ListNode x) {
		if (x.prev != null) {
			x.prev.next = x.next;
		} else {
			head = x.next;
		}

		if (x.next != null) {
			x.next.prev = x.prev;
		}
	}
	
	/*
	 * Convert a LinkedList to a string in the format of [#elements]
	 */
	public String toString () {
		String str;
		ListNode x;
		
		str = "[";
		x = this.head;
		while (x != null) {
			str += x.key + ", ";
			x = x.next;
		}
		
		str += "]";
		return str;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList l;
		
		l = new LinkedList();
		for (int i = 0; i < 5; i++)
			l.insert(i);
		System.out.println(l.toString());
		for (int i = 0; i < 2; i++) 
			l.delete(l.head.next);
		System.out.println(l.toString());
	}

}
