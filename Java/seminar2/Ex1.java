//Напишите метод, который принимает на вход строку (String) и определяет является ли строка палиндромом (возвращает boolean значение).

package seminar2;
import java.util.Scanner;
public class Ex1 {
    public static void main(String[] args) {
        String checkingString = getString();
        boolean pal = checkString(checkingString);
        System.out.printf("The string " + "'" + checkingString + "'" + "is a palindrome?  " + pal);
    }
    public static String getString(){
        Scanner lineScanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String getedString = lineScanner.next();
        return getedString;
    }
    public static boolean checkString(String checkedString){
        int length = checkedString.length();
        boolean pal = true;
        for (int i = 0; i < length/2 ; i++) {
            if (checkedString.charAt(i) != checkedString.charAt(length-1-i)){
                return false;
            }
        }
        return true;
    }
}

