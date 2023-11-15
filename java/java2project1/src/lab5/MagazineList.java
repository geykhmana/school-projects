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
   public String toString() {
      String result = "";
      Queue tempQueue = MagazineQueue;

      while (tempQueue.isEmpty() != true) {
         result += tempQueue.peek() + "\n";
         tempQueue.poll();
      }

      return result;
   }

   
}

/*class MagazineNode {
   public Magazine magazine;
   public MagazineNode next;

   //--------------------------------------------------------------
   //  Sets up the node
   //--------------------------------------------------------------
   public MagazineNode(Magazine mag) {
      magazine = mag;
      next = null;
   }
}*/
