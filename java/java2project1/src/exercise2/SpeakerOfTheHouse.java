package exercise2;

public class SpeakerOfTheHouse implements Speaker {
    public void speak() {
        System.out.println("I am the speaker of the house.");
    }

    public void announce(String bill) {
        System.out.println("The " + bill + " has passed!");
    }
}
