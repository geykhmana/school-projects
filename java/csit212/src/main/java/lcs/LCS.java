package lcs;

public class LCS {
	
	public static int lcs_length (String X, String Y) {
		int m = X.length();
		int n = Y.length();

		int[][] b = new int[m][n];
		int[][] c = new int[m + 1][n + 1];

		for (int i = 1; i < m+1; i++) {

		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(LCS.lcs_length("ABCBDAB", "BDCABA"));
		System.out.println(LCS.lcs_length("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA"));
	}

}
