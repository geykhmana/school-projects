package lab1;

import java.util.ArrayList;
import java.util.Scanner;

public class NumCounter {
    public static void main(String[] args) {
        ArrayList<Integer> intList = new ArrayList<Integer>();
        Scanner getNumInput = new Scanner(System.in);
        int i = 0;

        while (i < 7) {
            System.out.println("Enter an integer from 0 to 50 (inclusive): ");
            int newInt = getNumInput.nextInt();
            intList.add(newInt);
            i++;
        }

        System.out.println(intList);
    }
}
