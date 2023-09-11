package lab1;

import java.util.ArrayList;

public class QuantifyNums {

    public QuantifyNums(ArrayList<Integer> intList) {
        ArrayList<Integer> uniqueNums = new ArrayList<Integer>();
        ArrayList<Integer> quantOfNums = new ArrayList<Integer>();
        // Add  initial values to uniqueNums and quantOfNums so that the nested loop below works.
        uniqueNums.add((Integer) intList.get(0));
        quantOfNums.add(0);

        outerloop:
        for (int i = 0; i < intList.size(); i++) {
            System.out.println(intList.get(i));
            for (int j = 0; j < uniqueNums.size(); j++) {
                if (intList.get(i) == quantOfNums.get(j)) {
                    // If a duplicate number is found, log that in quantOfNums, then move to the next number in intList
                    int currentQuant = quantOfNums.get(j);
                    quantOfNums.set(j, currentQuant+1);
                    continue outerloop;
                } else {
                    // If not, move on to the next value in uniqueNums for comparison
                    j++;
                }
            }
            // If no match is found, log that in uniqueNames and quantOfNums
            uniqueNums.add((Integer) intList.get(i));
            quantOfNums.add(1);
        }

        String msgToReturn = "The numbers you entered were:";
        for (int j = 0; j < uniqueNums.size(); j++) {
            msgToReturn = msgToReturn + "\n" + uniqueNums.get(j) + " - " + quantOfNums.get(j) + " times";
        }
        System.out.println(msgToReturn);
    }
}
