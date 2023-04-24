package project2;
// ***************************************************************
// Shop.java
//
// Uses the Item class to create items and add them to a shopping
// cart stored in an ArrayList
// ***************************************************************
import java.util.ArrayList;
import java.util.Scanner;

public class Shop {
    public static void main(String[] args) {
        Item item;
        String itemName;
        double itemPrice;
        int quantity;
        int capacity;
        Item[] cart = new Item[capacity];
        Scanner scan = new Scanner(System.in);
        String keepShopping = "y";
        do {
            System.out.print("Enter the name of the item: ");
            itemName = scan.nextLine ();
            System.out.print("Enter the unit price: ");
            itemPrice = scan.nextDouble();
            System.out.print("Enter the quantity : ");
            quantity = scan.nextInt();
            // *** create a new item and add it to the cart
            Item item1 = new Item(itemName,itemPrice,quantity);
            // *** print the contents of the cart object using println
            System.out.println(item1);
            System.out.println("Continue shopping (y/n)? ");
            keepShopping = scan.nextLine();
        }
        while(keepShopping.equals ("y"));
    }
}