package overriding;

public class Messages {
   //-----------------------------------------------------------------
   //  Creates two objects and invokes the message method in each.
   //-----------------------------------------------------------------
   public static void main (String[] args) {
      Thought parked = new Thought();
      Advice dates = new Advice();
      parked.message();
      dates.message();  // overridden
   }
}
