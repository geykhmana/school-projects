package project2;
// ************************************************************
// Factorial.java
// Computes the factorial of a given integer
// ************************************************************
import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        int num;
        int printnum = 0;
        int answer = 1;

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a nonnegative integer: ");
        num = scan.nextInt();
        if (num < 0) {
            while (num < 0) {
                System.out.println("Please enter a nonnegative integer: ");
                num = scan.nextInt();
            }
        }
        if (num == 0) {
            answer = 1;
        } else {
            printnum = num;
            while (num > 0) {
                answer *= num;
                num--;
            }
        }

        System.out.println(printnum + "! = " + answer);
    }
}