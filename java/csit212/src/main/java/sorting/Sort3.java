package sorting;

import java.util.*;

public class Sort3 {
	public static int[] quick_sort (int[] array, int p, int r) {
		int q;
		if (p < r) {
			q = partition(array, p, r);
			quick_sort(array, p, q-1);
			quick_sort(array, q+1, r);
		}
		return array;
	}
	
	public static int partition (int[] array, int p, int r) {
		int x = array[r];
		int i = p - 1;

		for (int j = p; j < r; j++) {
			if (array[j] <= x) {
				i++;
				int temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
		}

		int temp2 = array[i + 1];
		array[i + 1] = array[r];
		array [r] = temp2;

		return i + 1;
	}
	
	public static int[] counting_sort (int[] array, int[] B, int k) {
		int[] C = new int[k+1];
		//int[] B = new int[0];

		for (int i = 0; i < k; i++) {
			C[i] = 0;
		}
		for (int j = 1; j < array.length; j++) {
			C[array[j]] += 1;
		}
		for (int i = 1; i <= k; i++) {
			C[i] += C[i-1];
		}
		for (int j = array.length-1; j > 1; j--) {
			B[C[array[j]]] = array[j];
			C[array[j]] -= 1;
		}

		return array;
	}
	
	
	public static int[] generate_random_array (int n, int k) {
		List<Integer> list;
		int[] array;
		Random rnd;
		
		rnd = new Random(System.currentTimeMillis());
		
		list = new ArrayList<Integer> ();
		for (int i = 1; i <= n; i++) 
			list.add(new Integer(rnd.nextInt(k+1)));
		
		Collections.shuffle(list, rnd);
		
		array = new int[n];
		for (int i = 0; i < n; i++) 
			array[i] = list.get(i).intValue();
		
		return array;
	} 
	
	public static int[] generate_random_array (int n) {
		List<Integer> list;
		int[] array;
		
		list = new ArrayList<Integer> ();
		for (int i = 1; i <= n; i++) 
			list.add(new Integer(i));
		
		Collections.shuffle(list, new Random(System.currentTimeMillis()));
		
		array = new int[n];
		for (int i = 0; i < n; i++) 
			array[i] = list.get(i).intValue();
		
		return array;
	}
	
	/*
	 * Input: an integer array
	 * Output: true if the array is acsendingly sorted, otherwise return false
	 */
	public static boolean check_sorted (int[] array) {
		for (int i = 1; i < array.length; i++) {
			if (array[i-1] > array[i])
				return false;
		}
		return true;
	}
	
	public static void print_array (int[] array) {
		for (int i = 0; i < array.length; i++)
			System.out.print(array[i] + ", ");
		System.out.println();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int k = 10000;
		
		System.out.println("Quick sort starts ------------------");
		for (int n = 100000; n <= 1000000; n=n+100000) {
			int[] array = Sort3.generate_random_array(n);
			long t1 = System.currentTimeMillis();
			array = Sort3.quick_sort(array, 0, n-1);
			long t2 = System.currentTimeMillis();
			long t = t2 - t1;
			boolean flag = Sort3.check_sorted(array);
			System.out.println(n + "," + t + "," + flag);
		}
		System.out.println("Quick sort ends ------------------");

		System.out.println("Counting sort starts ------------------");
		for (int n = 100000; n <= 1000000; n=n+100000) {
			int[] array = Sort3.generate_random_array(n, k);
			long t1 = System.currentTimeMillis();
			int[] B = new int[array.length];
			array = Sort3.counting_sort(array, B, k);
			long t2 = System.currentTimeMillis();
			long t = t2 - t1;
			boolean flag = Sort3.check_sorted(array);
			System.out.println(n + "," + t + "," + flag);
		}
		System.out.println("Counting sort ends ------------------");
	}
}

		

