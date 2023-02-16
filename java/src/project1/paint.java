package project1;

import java.util.Scanner;
public class paint {
    public static void main(String[] args) {
        final int COVERAGE = 350; //paint covers 350 sq ft/gal
        int length;
        int width;
        int height;
        int doors;
        int windows; //declare integers length, width, height, and windows;
        double totalSqFt; //declare double totalSqFt;
        double paintNeeded; //declare double paintNeeded;
        Scanner scan = new Scanner(System.in); //declare and initialize Scanner object
        System.out.println("Enter the length of the room: ");
        length = scan.nextInt(); //Prompt for and read in the length of the room
        System.out.println("Enter the width of the room: ");
        width = scan.nextInt(); //Prompt for and read in the width of the room
        System.out.println("Enter the height of the room: ");
        height = scan.nextInt(); //Prompt for and read in the height of the room
        System.out.println("Enter the number of doors in the room: ");
        doors = scan.nextInt(); //Prompt for and read in the amount of doors in the room
        System.out.println("Enter the number of windows in the room: ");
        windows = scan.nextInt(); //Prompt for and read in the amount of windows in the room
        totalSqFt = length * height * 2 + width * height * 2 - (doors * 20) - (windows * 15); //Compute the total square feet to be painted--think about the dimensions of each wall
        paintNeeded = totalSqFt / COVERAGE; //Compute the amount of paint needed
        System.out.println("The length of the room is " + length + " ft."); //Print the length, width, and height of the room and the number of gallons of paint needed.
        System.out.println("The width of the room is " + width + " ft.");
        System.out.println("The height of the room is " + height + " ft.");
        System.out.println(paintNeeded + " gallons of paint will be needed to paint the walls of the room.");
    }
}