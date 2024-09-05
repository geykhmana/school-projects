package exercise1;

public class ReadingMaterial {
    String title;
    String author;
    int numPages;

    public ReadingMaterial(String title, String author, int numPages) {
        this.title = title;
        this.author = author;
        this.numPages = numPages;
    }

    public boolean isLong() {
        if (numPages > 250) {
            return true;
        } else {
            return false;
        }
    }

    public void summary() {
        System.out.println(title + ", written by " + author);
    }
}
