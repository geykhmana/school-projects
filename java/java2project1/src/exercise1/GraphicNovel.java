package exercise1;

public class GraphicNovel extends Novel {
    public String illustrator;

    public GraphicNovel(String title, String author, int numPages, String character, String illustrator) {
        super(title, author, numPages, character);
        this.illustrator = illustrator;
    }

    public void summary() {
        System.out.println(title + ", written by " + author + ", illustrated by " + illustrator);
    }
}
