package lab2;

public class HospitalDriver {
    public static void main (String[] args) {
        Doctor doctor = new Doctor("Mark Boison", 1);
        Nurse nurse = new Nurse("Ruth Stein", 2);
        Receptionist receptionist = new Receptionist("Joe Fields", 3);
        Janitor janitor = new Janitor("Clara Clark", 4);
        Anesthesiologist anesthesiologist = new Anesthesiologist("Jaime Park", 5);

        System.out.println("The employees of the hospital are: " + doctor + ", " + nurse + ", " + receptionist + ", " + janitor + ", and " + anesthesiologist);

        doctor.work();
        nurse.work();
        receptionist.work();
        janitor.work();
        anesthesiologist.work();
    }
}
