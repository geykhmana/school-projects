package lab3;//********************************************************************
//  Contact.java       Author: Lewis/Loftus
//
//  Represents a phone contact.
//********************************************************************

public class Contact implements Comparable { // Has method compareTo
   private String firstName, lastName, phone;

   //-----------------------------------------------------------------
   //  Constructor: Sets up this contact with the specified data.
   //-----------------------------------------------------------------
   public Contact (String first, String last, String telephone) {
      firstName = first;
      lastName = last;
      phone = telephone;
   }

   //-----------------------------------------------------------------
   //  Returns a description of this contact as a string.
   //-----------------------------------------------------------------
   public String toString ()
   {
      return lastName + ", " + firstName + "\t" + phone;
   }

   //-----------------------------------------------------------------
   //  Returns a description of this contact as a string.
   //-----------------------------------------------------------------
   public boolean equals (Object other) {
      return (phone.equals(((Contact)other).getPhone()) &&
              lastName.equals(((Contact)other).getLastName()) &&
              firstName.equals(((Contact)other).getFirstName()));
              // Use String equals
   }
   //-----------------------------------------------------------------
   //  Uses both phone number and last and first names to determine ordering.
   //-----------------------------------------------------------------
   public int compareTo (Object other) {
      int result;

      String otherPhone = ((Contact)other).getPhone();
      String otherFirst = ((Contact)other).getFirstName();
      String otherLast = ((Contact)other).getLastName();

      if (phone.equals(otherPhone)) {
         if (lastName.equals(otherLast)) {
            result = firstName.compareTo(otherFirst);
         } else {
            result = lastName.compareTo(otherLast);
         }
      } else {
         result = phone.compareTo(otherPhone);
      }

      return result;
   }
   //-----------------------------------------------------------------
   //  First name accessor.
   //-----------------------------------------------------------------
   public String getFirstName ()
   {
      return firstName;
   }

   //-----------------------------------------------------------------
   //  Last name accessor.
   //-----------------------------------------------------------------
   public String getLastName ()
   {
      return lastName;
   }

   //-----------------------------------------------------------------
   //  Phone number accessor.
   //-----------------------------------------------------------------
   public String getPhone ()
   {
      return phone;
   }
}
