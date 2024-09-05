package exercise1;

public class Article extends ReadingMaterial {
    public String publication;

    public Article(String title, String author, int numPages, String publication) {
        super(title, author, numPages);
        this.publication = publication;
    }

    public void summary() {
        System.out.println(title + ", written by " + author + ", published in " + publication);
    }
}
