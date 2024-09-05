package lab2;

public class CoinDriver {
    public static void main (String[] args) {
        MonetaryCoin coin1 = new MonetaryCoin();
        MonetaryCoin coin2 = new MonetaryCoin();
        MonetaryCoin coin3 = new MonetaryCoin();

        coin1.setValue(5);
        coin2.setValue(10);
        coin3.setValue(25);

        int coinSum = coin1.getValue() + coin2.getValue() + coin3.getValue();

        System.out.println("The sum of the 3 coins is " + coinSum + ".");

        System.out.println("The initial face of the first coin is " + coin1);
        coin1.flip();
        System.out.println("The face of the first coin after flipping it is " + coin1);
    }
}
