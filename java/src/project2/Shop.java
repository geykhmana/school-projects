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
        String itemName;
        double itemPrice;
        int quantity;
        int capacity = 5;
        int i = 0;
        Item[] cart = new Item[capacity];
        Scanner scan = new Scanner(System.in);
        String keepShopping = "y";
        do {
            System.out.print("Enter the name of the item: ");
            itemName = scan.nextLine();
            System.out.print("Enter the unit price: ");
            itemPrice = scan.nextDouble();
            System.out.print("Enter the quantity: ");
            quantity = scan.nextInt();
            // *** create a new item and add it to the cart
            Item item1 = new Item(itemName, itemPrice, quantity);
            cart[i] = item1;
            // *** print the contents of the cart object using println
            for (int j=0;j<=i;j++) {
                System.out.println(cart[j]);
            }
            System.out.println("Continue shopping (y/n)? ");
            keepShopping = scan.nextLine();
            i++;
        }
        while(keepShopping.equals("y"));
    }
}