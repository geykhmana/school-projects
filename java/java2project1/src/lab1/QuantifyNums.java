package lab1;

import java.util.ArrayList;

public class QuantifyNums {
    public String QuantifyNums(ArrayList intList) {
        ArrayList<Integer> uniqueNums = new ArrayList<Integer>();
        ArrayList<Integer> quantOfNums = new ArrayList<Integer>();
        //Add an initial value to uniqueNums so that the nested loop below works.
        uniqueNums.add((Integer) intList.get(0));

        for (int i = 0; i < intList.size(); i++) {
            System.out.println(intList.get(i));
        }

        return null;
    }
}
