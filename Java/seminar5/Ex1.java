//Реализуйте структуру телефонной книги с помощью HashMap, учитывая, что 1 человек может иметь несколько телефонов.
package seminar5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        HashMap <String, ArrayList<String>> phonebook = new HashMap<>();
        while (true) {
            Scanner readLine = new Scanner(System.in);
            System.out.println("Enter a name: ");
            Scanner lineScanner = new Scanner(System.in);
            String name = lineScanner.next();
            System.out.println("Enter a number: ");
            String number = lineScanner.next();
            if (phonebook.containsKey(name) && phonebook.get(name).contains(number)) {
                System.out.printf("The name %s and number %s already in the phonebook \n", name, number);
            } else if (phonebook.containsKey(name) && !phonebook.get(name).contains(number)) {
                phonebook.get(name).add(number);
            } else {
                ArrayList<String> numbers = new ArrayList<>();
                numbers.add(number);
                phonebook.put(name, numbers);
            }
            System.out.println("Would you like to add another entry? Enter 'n' to exit or any other to continue");
            String useranswer = lineScanner.next();
            if (useranswer.equals("n")){
                break;
            }
            System.out.println(phonebook);
        }


    }
}
