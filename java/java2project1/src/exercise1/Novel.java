package exercise1;

import java.util.ArrayList;

public class Novel extends ReadingMaterial {
    public ArrayList<String> characters;

    public Novel(String title, String author, int numPages, String character) {
        super(title, author, numPages);
        characters.add(character);
    }

    public void listCharacters() {
        for (int i = 0; i < characters.size(); i++) {
            System.out.println(characters.get(i));
        }
    }
}
