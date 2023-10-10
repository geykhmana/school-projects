package exercise2;

import java.util.Scanner;

public class Driver {
    public static void main(String[] args) {
        Scanner getInput = new Scanner(System.in);

        String bill = getInput.nextLine();
        String team = getInput.nextLine();
        String movie = getInput.nextLine();

        SpeakerOfTheHouse alan = new SpeakerOfTheHouse(); //Since there is no US speaker of the house, I had to step in.
        alan.speak();
        alan.announce(bill);

        SportsAnnouncer tony = new SportsAnnouncer();
        tony.speak();
        tony.announce(team);

        Actor leoDiCaprio = new Actor();
        leoDiCaprio.speak();
        leoDiCaprio.announce(movie);
    }
}
