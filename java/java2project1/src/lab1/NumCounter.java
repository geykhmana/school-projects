package lab1;

import java.util.ArrayList;
import java.util.Scanner;

public class NumCounter {
    public static void main(String[] args) {
        ArrayList<Integer> intList = new ArrayList<Integer>();
        Scanner getNumInput = new Scanner(System.in);
        int i = 0;

        System.out.println("Enter the amount of numbers you would like to enter: ");
        int amntOfNums = getNumInput.nextInt();

        while (i < amntOfNums) {
            System.out.println("Enter an integer from 0 to 50 (inclusive): ");
            int newInt = getNumInput.nextInt();
            if (newInt >= 0 && newInt <= 50) {
                intList.add(newInt);
                i++;
            } else {
                System.out.println("The number you entered was not within the range 0-50. Please try again.\n");
                continue;
            }
        }

        QuantifyNums quantifyNums = new QuantifyNums(intList);
    }
}
