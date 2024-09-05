package project2;
// *************************************************************** // ShoppingCart.java
// Represents a shopping cart as an array of items
// ***************************************************************
import java.text.NumberFormat;
public class ShoppingCart {
    private int itemCount; // total number of items in the cart
    private double totalPrice; // total price of items in the cart
    private int capacity; // current cart capacity
    private Item cart[];

    // Creates an empty shopping cart with a capacity of 5 items.
    public ShoppingCart() {
        capacity = 5;
        //create an array of Item type of capacity 5
        cart = new Item[capacity];
        //set itemCount and totalPrice to zero
        itemCount = 0;
        totalPrice = 0.0;
    }

    // Adds an item to the shopping cart.
    public void addToCart(String itemName, double price, int quantity) {
        //instatiate a Item class object with three input
        //parameters called itemName, price and quantity
        if (itemCount < capacity) {
            cart[itemCount] = new Item(itemName, price, quantity);
            //incremnt the itemCount by one
            itemCount++;
        } else {
            //increaseSize();
            cart[itemCount] = new Item(itemName, price, quantity);
            //increment the itemCount by one
            itemCount++;
        }
    }

    // Returns the contents of the cart together with
    // summary information.
    public String toString() {
        NumberFormat fmt = NumberFormat.getCurrencyInstance();
        String contents = "\nShopping Cart\n";
        contents += "\nItem\tUnit Price\tQuantity\tTotal\n";

        for (int i = 0; i < itemCount; i++) {
            contents += cart[i].toString() + "\n";
        }
        return contents;
    }

    //The method getTotalCost that calculates the total price
//of all items in the cart and returns totalPrice
    public double getTotalCost() {
        for (int count = 0; count < itemCount; count++) {
            totalPrice += cart[count].getPrice() * cart[count].getQuantity();
        }
        return totalPrice;
    }
}