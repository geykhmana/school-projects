package exercise2;

public class Actor implements Speaker {
    public void speak() {
        System.out.println("I've been nominated for three Academy Awards.");
    }

    public void announce(String movie) {
        System.out.println("I'm currently starring in " + movie);
    }
}
