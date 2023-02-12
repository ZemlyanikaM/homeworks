package seminar4;
//Реализовать консольное приложение, которое:
//Принимает от пользователя и “запоминает” строки.
//Если введено print, выводит строки так, чтобы последняя введенная была первой в списке, а первая - последней.
//Если введено revert, удаляет предыдущую введенную строку из памяти.
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;
public class Ex1 {
    public static void main(String[] args) {
        userInterface();
    }
    private static void userInterface(){
        Scanner lineScanner = new Scanner(System.in);
        Deque<String> deque = new ArrayDeque<>();
        String userString = "";
        while(true){
            System.out.println("Emter any string to save it. " +
                    "\nEnter 'print' to see the list of strings. " +
                    "\nEnter 'revert' to remove the last string from the list" +
                    "\nEnter 'quit' to exit" );
            userString = lineScanner.next();
            if (userString.equals("print")){
                if (deque.size() > 0) {
                    System.out.println(deque + "\n");
                } else{
                    System.out.println("Nothhing to print. The list is empty\n");
                }
            } else if (userString.equals("revert")){
                if (deque.size() > 0){
                    deque.removeFirst();
                } else{
                    System.out.println("Nothhing to remove. The list is empty\n");
                }

            } else if (userString.equals("quit")){
                break;
            }else {
                deque.addFirst(userString);
            }

        }
    }
}
