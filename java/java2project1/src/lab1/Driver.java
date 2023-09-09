package lab1;

public class Driver {
    public static void main(String[] args) {
        Problem p1 = new Problem();
        p1.setLevel(3);
        System.out.println("The difficulty level of problem 1 is " + p1.getLevel() + ".");

        Problem p2 = new Problem();
        p2.setLevel(5);
        System.out.println("The difficulty level of problem 2 is " + p2.getLevel() + ".");

        Problem p3 = new Problem();
        p3.setLevel(9);
        System.out.println("The difficulty level of problem 3 is " + p3.getLevel() + ".");
    }
}
