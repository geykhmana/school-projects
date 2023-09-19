package lab2;
public class Nurse {
    protected String name;
    protected int number;

    //-----------------------------------------------------------------
    //  Sets up this hospital employee with the specified information.
    //-----------------------------------------------------------------
    public Nurse (String empName, int empNumber) {
        name = empName;
        number = empNumber;
    }

    //-----------------------------------------------------------------
    //  Sets the name for this employee.
    //-----------------------------------------------------------------
    public void setName (String empName) {
        name = empName;
    }

    //-----------------------------------------------------------------
    //  Sets the employee number for this employee.
    //-----------------------------------------------------------------
    public void setNumber (int empNumber) {
        number = empNumber;
    }

    //-----------------------------------------------------------------
    //  Returns this employee's name.
    //-----------------------------------------------------------------
    public String getName() {
        return name;
    }

    //-----------------------------------------------------------------
    //  Returns this employee's number.
    //-----------------------------------------------------------------
    public int getNumber() {
        return number;
    }

    //-----------------------------------------------------------------
    //  Returns a description of this employee as a string.
    //-----------------------------------------------------------------
    public String toString() {
        return name + "\t" + number;
    }

    //-----------------------------------------------------------------
    //  Prints a message appropriate for this employee.
    //-----------------------------------------------------------------
    public void work() {
        System.out.println (name + " is a nurse at the hospital.");
    }
}
