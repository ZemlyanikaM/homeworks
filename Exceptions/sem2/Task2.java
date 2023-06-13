/*
Если необходимо, исправьте данный код:
try {
   int d = 0;
   double catchedRes1 = intArray[8] / d;
   System.out.println("catchedRes1 = " + catchedRes1);
} catch (ArithmeticException e) {
   System.out.println("Catching exception: " + e);
}
 */
package sem2.hw;

public class Task2 {
    public static void main(String[] args) {
        int d = 45;
        double[] intArray = {0, 1, 2, 3, 4, 5, 6, 7, 8};
        int index = 65;
        if (intArray.length < index) {
            System.out.printf("The index " + index + " is outside the bounds of the array ");
        } else if (d == 0) {
            System.out.printf("Error! Dividing by zero!");
        } else {
            double catchedRes1 = intArray[index] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        }
    }
}
