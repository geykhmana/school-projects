package hw6;

public class RodCut {
	int n;
	int[] p;
	int[] r;
	int[] s;
	
	public RodCut () {
		n = 10;
		p = new int[11];
		p[0] = 0;
		p[1] = 1;
		p[2] = 5;
		p[3] = 8;
		p[4] = 9;
		p[5] = 10;
		p[6] = 17;
		p[7] = 17;
		p[8] = 20;
		p[9] = 24;
		p[10] = 30;
	}
	
	public int memoized_cut_rod () {
    
      
	}
	
	public int memoized_cut_rod_aux (int p[], int n, int r[]) {
   
	}
	
	public int bottom_up_cut_rod () {
 
					
	}
	
	public void extended_bottom_up_cut_rod () {
   
	}
	
	public void print_cut_rod_solution () {
		for (int i = 0; i <= n; i++) {
			System.out.print(i + "\t");
		}
		System.out.print("\n");
		for (int i = 0; i <= n; i++) {
			System.out.print(r[i] + "\t");
		}
		System.out.print("\n");
		for (int i = 0; i <= n; i++) {
			System.out.print(s[i] + "\t");
		}
		System.out.print("\n");
	}
	

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RodCut rc;
		
		rc = new RodCut();
		System.out.println("memoized_cut_rod starts ------------------");
		System.out.println(rc.memoized_cut_rod());
		System.out.println("memoized_cut_rod ends ------------------");
		System.out.print("\n\n");
		
		System.out.println("bottom_up_cut_rod starts ------------------");
		System.out.println(rc.bottom_up_cut_rod());
		System.out.println("bottom_up_cut_rod ends ------------------");
		System.out.print("\n\n");

		System.out.println("extended_bottom_up_cut_rod starts ------------------");
		rc.extended_bottom_up_cut_rod();
		rc.print_cut_rod_solution();
		System.out.println("extended_bottom_up_cut_rod ends ------------------");
		System.out.print("\n\n");
	}

}