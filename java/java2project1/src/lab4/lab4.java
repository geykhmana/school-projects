package lab4;
import java.util.Arrays;
import java.util.Scanner;

public class lab4 {
    public static void main(String[] args) {
        int[] triangleLine = new int[]{1};
        int[] triangleLine2 = new int[]{1, 1};
        int lastIndex = 0;
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
            int[] previousLine = triangleLine2;
            
            for (int i = 0; i < n; i++) {
                triangleLine = new int[]{1};
                for (int j = 1; j < previousLine.length-1; j++) {
                    triangleLine[j] = previousLine[j-1] + previousLine[j];
                    lastIndex = j+1; /* Allows for the last 1 to be added to the line after the loop */
                }
                triangleLine[lastIndex] = 1;
                previousLine = triangleLine;
            }
        }

        System.out.println("If N = " + n + ", then the Nth line of Pascal's triangle is:\n" + Arrays.toString(triangleLine));
    }
}
