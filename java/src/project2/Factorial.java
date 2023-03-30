package project2;
// Factorial.java

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        int num;
        int answer = 1;

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a nonnegative integer: ");
        num = scan.nextInt();
        int printnum = num;
        if (num == 0 || num == 1) {
            answer = 1;
        } else {
            while (num > 1) {
                answer *= num;
                num--;
            }
        }

        System.out.println(printnum + "! = " + answer);
    }
}