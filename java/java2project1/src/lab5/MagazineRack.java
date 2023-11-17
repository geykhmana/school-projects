package lab5;

public class MagazineRack {
   //----------------------------------------------------------------
   //  Creates a MagazineList object, adds several magazines to the
   //  list, then prints it.
   //----------------------------------------------------------------
   public static void main(String[] args) {
      MagazineList rack = new MagazineList();
      
      rack.add(new Magazine("Newsweek")); // Added so it can be removed
      rack.add(new Magazine("Time"));
      rack.add(new Magazine("Woodworking Today"));
      rack.add(new Magazine("Communications of the ACM"));
      rack.add(new Magazine("House and Garden"));
      rack.add(new Magazine("GQ"));

      //rack.remove();    // Removes the first item in the queue

      System.out.println(rack); 
   }
}