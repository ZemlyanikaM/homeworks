/*
Дан следующий код, исправьте его там, где требуется:
public static void main(String[] args) throws Exception {
   try {
       int a = 90;
       int b = 3;
       System.out.println(a / b);
       printSum(23, 234);
       int[] abc = { 1, 2 };
       abc[3] = 9;
   } catch (Throwable ex) {
       System.out.println("Что-то пошло не так...");
   } catch (NullPointerException ex) {
       System.out.println("Указатель не может указывать на null!");
   } catch (IndexOutOfBoundsException ex) {
       System.out.println("Массив выходит за пределы своего размера!");
   }
}
public static void printSum(Integer a, Integer b) throws FileNotFoundException {
   System.out.println(a + b);
}
 */
package sem2.hw;

public class Task3 {
    public static void main(String[] args) throws Exception {
        int a = 90;
        int b = 3;
        if (b != 0) {
            System.out.println(a / b);
        } else {
            System.out.println("Error! Dividing by zero!");
        }
        printSum(23, 234);

        int[] abc = {1, 2};
        int index = 3;
        if (index < abc.length) {
            abc[index] = 9;
        } else {
            System.out.printf("The index " + index + " is outside the bounds of the array ");
        }
    }
    public static void printSum(Integer a, Integer b) {
        System.out.println(a + b);
    }
}
