package project1;
// ************************************************************
// Student.java
//
// Define a student class that stores name, score on test 1, and
// score on test 2. Methods prompt for and read in grades,
// compute the average, and return a string containing student’s info.
// ************************************************************
import java.util.Scanner;
public class Student {
    //declare instance data
    private String name;
    private int test1 = 0;
    private int test2 = 0;
    //constructor
    // ---------------------------------------------
    public Student(String studentName) {
        name = studentName;
    }
        // ---------------------------------------------
    //inputGrades: prompt for and read in student’s grades for test1 and test2.
    //Use name in prompts, e.g., "Enter’s Joe’s score for test1".
    // ---------------------------------------------
    public void inputGrades() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter " + name + "'s score for test1: ");
        test1 = scan.nextInt();
        System.out.println("Enter " + name + "'s score for test2: ");
        test2 = scan.nextInt();
    }
        // ---------------------------------------------
    //getAverage: compute and return the student’s test average
    public double getAverage() {
        return (test1+test2) / 2;
    }
        // ---------------------------------------------
    //getName: print the student’s name
    // ---------------------------------------------
    public String getName() {
        return name;
    }
}