package hw10;

import hw9.PrimNode;

import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Graph3 {
	int n;
	int[][] A;
	int[] d;	//shortest distance
	/*
	 * @param args
	 */
	
	public Graph3 () {
		
	}
	
	public Graph3 (int _n, int[][] _A) {
		n = _n;
		A = _A;
		d = new int[n];
	}
	
	public void initialize_single_source(int s) {
		for (int i = 0; i < n; i++)
			d[i] = Integer.MAX_VALUE;
		d[s] = 0;
	}
	
	public void relax (int u, int v) {
		if (d[v] > (d[u] + A[u][v])) 
			d[v] = d[u] + A[u][v];
	}
	
	public boolean bellman_ford (int s) {
		initialize_single_source(s);
		int[] e;
		for (int i = 1; i < n-1; i++) {
			for (int j = 1; j < n-1; j++) {
				relax(i, j);
			}
		}
		for (int u = 1; u < n-1; u++) {
			for (int v = 1; v < n-1; v++) {
				if (d[v] > d[u] + A[u][v]) {
					return false;
				}
			}
		}
		return true;
	}
	
	public void dijkstra (int s) {
		initialize_single_source(s);
		Queue<Integer> S = new LinkedList<>();
		Queue<Integer> Q = new LinkedList<Integer>();
		Q.add(s);
		while (!Q.isEmpty()) {
			int u = Q.poll();
			for (int v = 0; v < n; v++) {

				relax(u, v);
			}
		}
	}
	
	public void display_distance () {
		for (int i = 0; i < n; i++)
			System.out.println(i + ": " + d[i]);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 5;
		int[][] A = {
		{0, 6, 0, 7, 0},
		{0, 0, 5, 8, -4},
		{0, -2, 0, 0, 0},
		{0, 0, -3, 0, 9},
		{2, 0, 7, 0, 0}
		};
		Graph3 g1 = new Graph3(n, A);
		g1.bellman_ford(0);
		g1.display_distance();
		
		System.out.println("-----------------------");
		
		int[][] B = {
		{0, 10, 0, 5, 0},
		{0, 0, 1, 2, 0},
		{0, 0, 0, 0, 4},
		{0, 3, 9, 0, 2},
		{7, 0, 6, 0, 0}
		};
		Graph3 g2 = new Graph3(n, B);
		g2.dijkstra(0);
		g2.display_distance();
	}

}
