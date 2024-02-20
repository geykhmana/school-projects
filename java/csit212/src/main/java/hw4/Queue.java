package hw4;

public class Queue {
	
	public int size;
	public int[] array;
	public int head;
	public int tail;
	
	public Queue () {
		size = 0;
		array = null;
		head = 0;
		tail = 0;
	}
	
	public Queue (int _size) {
		size = _size;
		array = new int[size];
		head = 0;
		tail = 0;
	}
	
	/*
	 * Implement the ENQUEUE(Q, x) function
	 */
	public void enqueue (int x) {
		
	}
	
	/*
	 * Implement the DEQUEUE(Q) function
	 */
	public int dequeue () {
		
	}
	
	/*
	 * Convert queue to string in the format of #size, head, tail, [#elements]
	 */
	public String toString () {
		String str;
		
		str = size + ", " + head + ", " + tail + ", [";
		for (int i = head; i%size < tail; i++) 
			str += array[i] + ",";
		
		str += "]";
		return str;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue q;
		
		q = new Queue(10);
		for (int i = 0; i < 5; i++)
			q.enqueue(i);
		System.out.println(q.toString());
		for (int i = 0; i < 2; i++) 
			q.dequeue();
		System.out.println(q.toString());
	}

}
