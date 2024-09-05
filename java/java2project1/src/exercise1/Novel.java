package exercise1;

import java.util.ArrayList;

public class Novel extends ReadingMaterial {
    public String[] characters;

    public Novel(String title, String author, int numPages, String[] characters) {
        super(title, author, numPages);
        this.characters = characters;
    }

    public void listCharacters() {
        for (int i = 0; i < characters.length; i++) {
            System.out.println(characters[i]);
        }
    }
}
