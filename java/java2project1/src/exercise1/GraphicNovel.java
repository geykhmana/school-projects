package exercise1;

public class GraphicNovel extends Novel {
    public String illustrator;

    public GraphicNovel(String title, String author, int numPages, String[] characters, String illustrator) {
        super(title, author, numPages, characters);
        this.illustrator = illustrator;
    }

    public void summary() {
        System.out.println(title + ", written by " + author + ", illustrated by " + illustrator);
    }
}
