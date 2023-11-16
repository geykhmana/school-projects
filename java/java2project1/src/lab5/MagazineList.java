package lab5;

import java.util.LinkedList;
import java.util.Queue;

public class MagazineList {
   Queue<Magazine> MagazineQueue = new LinkedList<Magazine>();

   public MagazineList() {

   }

   public void add(Magazine mag) {
      MagazineQueue.add(mag);
   }
   public void remove() {
      MagazineQueue.poll();
   }

   public String toString() {
      String result = "";
      Queue tempQueue = new LinkedList();

      for (Object i : MagazineQueue.toArray()) {
         tempQueue.add(i);
      }

      while (tempQueue.isEmpty() != true) {
         result += tempQueue.peek() + "\n";
         tempQueue.poll();
      }

      return result;
   }

   
}
