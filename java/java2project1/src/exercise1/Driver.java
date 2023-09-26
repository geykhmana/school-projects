package exercise1;

public class Driver {
    public static void main (String[] args) {
        Novel harryPotter = new Novel("Harry Potter", "JK Rowling", 303, new String[]{"Harry Potter", "Hermione Granger", "Ronald Weasley", "Voldemort"});
        GraphicNovel avengers = new GraphicNovel("Avengers", "Stan Lee", 50, new String[]{"Iron Man", "Captain America", "Black Widow", "The Hulk", "Thor"}, "Jack Kirby");
        Article pc = new Article("The Social Meaning of the Personal Computer", "Bryan Pfaffenberger", 10, "Anthropological Quarterly");

        harryPotter.summary();
        System.out.println(harryPotter.isLong());

        avengers.listCharacters();

        System.out.println(pc.isLong());
        pc.summary();
    }
}
