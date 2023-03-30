package project2;
// ************************************************************
// Salary.java
// Computes the raise and new salary for an employee
// ************************************************************
import java.util.Scanner;
public class Salary {
    public static void main (String[] args) {
        double currentSalary; // current annual salary
        double rating; // performance rating
        double raise; // dollar amount of the raise
        double newSalary; // new salary for the employee

        Scanner scan = new Scanner(System.in);

        // Get the current salary and performance rating
        System.out.print("Enter the current salary: ");
        currentSalary = scan.nextDouble();

        // Compute the raise -- Use if ... else ...
        newSalary = currentSalary + raise;

        // Print the results

        NumberFormat money = NumberFormat.getCurrencyInstance();
        System.out.println();
        System.out.println("Current Salary: " + money.format(currentSalary));
        System.out.println("Amount of your raise: " + money.format(raise));
        System.out.println( "Your new salary: " + money.format(newSalary));
        System.out.println();
    }
}