package lab5;

public class MagazineList {
   private MagazineNode front, rear;

   //----------------------------------------------------------------
   //  Sets up an initially empty list of magazines.
   //----------------------------------------------------------------
   public MagazineList() {
      front = rear = null;
   }
   //----------------------------------------------------------------
   //  Creates a new MagazineNode object and adds it to the end of
   //  the linked list.
   //----------------------------------------------------------------
   public void enqueue(Magazine mag) {
      MagazineNode node = new MagazineNode(mag);
      MagazineNode current;

      if (rear == null) {
         front = rear = node;
      } else {
         current = rear;
         while (current.next != null) {
            current = current.next;
         }
         current.next = node;
      }
   }
   public void dequeue() {
      MagazineNode current = front.next;

      if (front == null) {
         return;
      }

      front.next = null;
      front = current;

      if (front == null) {
         rear = null;
      }
   }
   public boolean empty() {
      MagazineNode current = front;

      while (current == null) {
         current = current.next;
      }

      if (current != null) {
         return false;
      } else {
         return true;
      }
   }
   public String toString() {
      String result = "";

      MagazineNode current = front;

      while (current != null) {
         result += current.magazine + "\n";
         current = current.next;
      }

      return result;
   }
   //*****************************************************************
   //  An inner class that represents a node in the magazine list.
   //  The public variables are accessed by the MagazineList class.
   //*****************************************************************
   
}

class MagazineNode {
   public Magazine magazine;
   public MagazineNode next;

   //--------------------------------------------------------------
   //  Sets up the node
   //--------------------------------------------------------------
   public MagazineNode(Magazine mag) {
      magazine = mag;
      next = null;
   }
}
