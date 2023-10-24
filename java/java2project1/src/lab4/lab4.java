package lab4;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class lab4 {
    public static void main(String[] args) {
        ArrayList<Integer> triangleLine = new ArrayList<Integer>();
        triangleLine.add(1);
        ArrayList<Integer> triangleLine2 = new ArrayList<Integer>();
        triangleLine2.add(1);
        triangleLine2.add(1);
        Scanner getN = new Scanner(System.in);
        
        System.out.println("Please enter a positive integer: ");
        int n = getN.nextInt();

        if (n == 1) {
            /* triangleLine is already set to the first line */
        } else if (n == 2) {
            triangleLine = triangleLine2;
        } else if (n < 1) {
            System.out.println("Invalid number");
        } else {
            ArrayList<Integer> previousLine = triangleLine2;
            
            while (triangleLine.size() < n) {
                triangleLine.clear();
                triangleLine.add(1);
                for (int j = 1; j <= previousLine.size(); j++) {
                    triangleLine.add(previousLine.get(j-1) + previousLine.get(j));
                }
                triangleLine.add(1);
                previousLine = triangleLine;
            }
        }

        System.out.println("If N = " + n + ", then the Nth line of Pascal's triangle is:\n" + triangleLine);
    }
}