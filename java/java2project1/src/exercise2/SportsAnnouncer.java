package exercise2;

public class SportsAnnouncer implements Speaker {
    public void speak() {
        System.out.println("Goal!");
    }

    public void announce(String team) {
        System.out.println("The " + team + " have scored a goal!");
    }
}
