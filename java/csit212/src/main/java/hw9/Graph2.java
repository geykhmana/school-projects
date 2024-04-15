package hw9;
import java.util.*;

public class Graph2 {
	
	public int n;	//number of vertice
	public int[][] A;	//the adjacency matrix
	
	public Graph2 () {
		n = 0;
		A = null;
	}
	
	public Graph2 (int _n, int[][] _A) {
		this.n = _n;
		this.A = _A;
	}
	
	public int prim (int r) {
		
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 9;
		int A[][] = {
				{0, 4, 0, 0, 0, 0, 0, 8, 0}, 
				{4, 0, 8, 0, 0, 0, 0, 11, 0}, 
				{0, 8, 0, 7, 0, 4, 0, 0, 2}, 
				{0, 0, 7, 0, 9, 14, 0, 0, 0}, 
				{0, 0, 0, 9, 0, 10, 0, 0, 0}, 
				{0, 0, 4, 14, 10, 0, 2, 0, 0}, 
				{0, 0, 0, 0, 0, 2, 0, 1, 6}, 
				{8, 11, 0, 0, 0, 0, 1, 0, 7}, 
				{0, 0, 2, 0, 0, 0, 6, 7, 0} 
		};
		Graph2 g = new Graph2(n, A);
		System.out.println(g.prim(0));
	}

}
