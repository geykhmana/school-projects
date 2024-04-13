package hw8;

import java.util.Queue;
import java.util.LinkedList;

public class Graph {
	public int n;	//number of vertices
	public int[][] A;	//the adjacency matrix
	private final int WHITE = 2;
	private final int GRAY = 3;
	private final int BLACK = 4;
	
	public Graph () {
		n = 0;
		A = null;
	}
	
	public Graph (int _n, int[][] _A) {
		this.n = _n;
		this.A = _A;
	}
	
	/*
	 * Input: s denotes the index of the source node
	 * Output: the array dist, where dist[i] is the distance between the i-th node to s
	 */
	public int[] bfs (int s) {
		int[] color = new int[n];
		int[] d = new int[n];
		for (int u = 0; u < n; u++) {
			color[u] = WHITE;
			d[u] = Integer.MAX_VALUE;
		}
		color[s] = GRAY;
		d[s] = 0;
		Queue<Integer> Q = new LinkedList<Integer>();
		Q.add(s);
		while (!Q.isEmpty()) {
			int u = Q.poll();
			for (int v = 0; v < n; v++) {
				if (A[u][v] == 1 && color[v] == WHITE) {
					color[v] = GRAY;
					d[v] = d[u] + 1;
					Q.add(v);
				}
			}
			color[u] = BLACK;
		}
		return d;
	}
	
	public void print_array (int[] array) {
		for (int i = 0; i < array.length; i++)
			System.out.println(i + ": " + array[i]);
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 8;
		int[][] A = 
			{{0, 1, 0, 0, 1, 0, 0, 0},
			{1, 0, 0, 0, 0, 1, 0, 0},
			{0, 0, 0, 1, 0, 1, 1, 0},
			{0, 0, 1, 0, 0, 0, 1, 1},
			{1, 0, 0, 0, 0, 0, 0, 0},
			{0, 1, 1, 0, 0, 0, 1, 0},
			{0, 0, 1, 1, 0, 1, 0, 1},
			{0, 0, 0, 1, 0, 0, 1, 0}};
		Graph g = new Graph(n, A);
		g.print_array(g.bfs(1));
	}

}
