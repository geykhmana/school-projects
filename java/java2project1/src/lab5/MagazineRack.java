package lab5;

public class MagazineRack {
   //----------------------------------------------------------------
   //  Creates a MagazineList object, adds several magazines to the
   //  list, then prints it.
   //----------------------------------------------------------------
   public static void main(String[] args) {
      MagazineList rack = new MagazineList();

      rack.enqueue(new Magazine("Time"));
      rack.enqueue(new Magazine("Woodworking Today"));
      rack.enqueue(new Magazine("Communications of the ACM"));
      rack.enqueue(new Magazine("House and Garden"));
      rack.enqueue(new Magazine("GQ"));
      rack.enqueue(new Magazine("Newsweek"));

      rack.dequeue();    // Removes the first item in the queue

      System.out.println(rack.empty());

      System.out.println(rack);
   }
}